import requests
from urllib.parse import urljoin, urlparse
import os
from bs4 import BeautifulSoup
import mimetypes
import json

class IconDownloader:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def get_icon_sources(self, url):
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            
            icons = []
            
            # Check for PWA manifest
            manifest_link = soup.find('link', rel='manifest')
            if manifest_link:
                manifest_url = urljoin(url, manifest_link.get('href', ''))
                try:
                    manifest_response = requests.get(manifest_url, headers=self.headers)
                    manifest_data = json.loads(manifest_response.text)
                    if 'icons' in manifest_data:
                        for icon in manifest_data['icons']:
                            if 'src' in icon:
                                icons.append({
                                    'url': urljoin(url, icon['src']),
                                    'size': icon.get('sizes', '0x0').split('x')[0],
                                    'type': icon.get('type', '')
                                })
                except:
                    pass

            # Apple touch icons (usually high quality)
            apple_touch_icons = soup.find_all('link', rel=lambda r: r and 'apple-touch-icon' in r)
            for icon in apple_touch_icons:
                size = icon.get('sizes', '0x0').split('x')[0]
                icons.append({
                    'url': urljoin(url, icon['href']),
                    'size': size,
                    'type': icon.get('type', '')
                })

            # Standard favicon links
            favicon_links = soup.find_all('link', rel=lambda r: r and ('icon' in r or 'shortcut' in r))
            for icon in favicon_links:
                size = icon.get('sizes', '0x0').split('x')[0]
                icons.append({
                    'url': urljoin(url, icon['href']),
                    'size': size,
                    'type': icon.get('type', '')
                })

            # Default favicon.ico
            icons.append({
                'url': urljoin(url, '/favicon.ico'),
                'size': '0',
                'type': 'image/x-icon'
            })

            # Sort icons by size (largest first)
            icons.sort(key=lambda x: int(x['size']) if x['size'].isdigit() else 0, reverse=True)
            
            return icons

        except Exception as e:
            print(f"Error fetching icons: {str(e)}")
            return []

    def download_favicon(self, domain):
        try:
            # Extract subdomain name for filename
            subdomain = domain.split('.')[0]
            
            # Add https:// if not present
            url = f"https://{domain}" if not domain.startswith(('http://', 'https://')) else domain
            
            icons = self.get_icon_sources(url)
            
            if not icons:
                print(f"No icons found for {domain}")
                return

            # Try downloading icons in order until successful
            for icon in icons:
                try:
                    response = requests.get(icon['url'], headers=self.headers, timeout=10)
                    response.raise_for_status()
                    
                    # Verify we got an image
                    content_type = response.headers.get('content-type', '')
                    if not content_type.startswith('image/'):
                        continue

                    # Determine file extension
                    extension = mimetypes.guess_extension(content_type)
                    if not extension:
                        if 'png' in content_type:
                            extension = '.png'
                        elif 'jpeg' in content_type or 'jpg' in content_type:
                            extension = '.jpg'
                        elif 'ico' in content_type:
                            extension = '.ico'
                        else:
                            extension = '.png'

                    # Create filename
                    filename = f"{subdomain}{extension}"
                    
                    # Save the file
                    with open(filename, 'wb') as f:
                        f.write(response.content)
                    
                    print(f"Successfully downloaded {filename} (Size: {icon['size']}px)")
                    return
                    
                except Exception as e:
                    continue

            print(f"Failed to download any icons for {domain}")

        except Exception as e:
            print(f"Error processing {domain}: {str(e)}")

def process_domains(domains):
    # Create output directory if it doesn't exist
    os.makedirs('favicons', exist_ok=True)
    os.chdir('favicons')
    
    downloader = IconDownloader()
    
    # Process each domain
    for domain in domains:
        domain = domain.strip()
        if domain:
            downloader.download_favicon(domain)

# Example usage
if __name__ == "__main__":
    domains = """

    """.strip().split('\n')
    
    process_domains([d.strip() for d in domains if d.strip()])
