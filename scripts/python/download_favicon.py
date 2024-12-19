import requests
from urllib.parse import urlparse
import os
from bs4 import BeautifulSoup
import favicon
import mimetypes

def download_favicon(domain):
    try:
        # Extract subdomain name for filename
        subdomain = domain.split('.')[0]
        
        # Add https:// if not present
        url = f"https://{domain}" if not domain.startswith(('http://', 'https://')) else domain
        
        # Get all favicon icons
        icons = favicon.get(url)
        
        if not icons:
            print(f"No favicon found for {domain}")
            return
        
        # Get the best quality icon (usually the last one)
        icon = icons[-1]
        
        # Download the icon
        response = requests.get(icon.url, stream=True)
        response.raise_for_status()
        
        # Determine file extension from content-type
        content_type = response.headers.get('content-type')
        extension = mimetypes.guess_extension(content_type) or '.ico'
        
        # Clean up extension
        extension = extension.replace('.jpeg', '.jpg')
        if extension == '.ico' and content_type == 'image/png':
            extension = '.png'
        
        # Create filename
        filename = f"{subdomain}{extension}"
        
        # Save the file
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print(f"Successfully downloaded {filename}")
        
    except Exception as e:
        print(f"Error downloading favicon for {domain}: {str(e)}")

def process_domains(domains):
    # Create output directory if it doesn't exist
    os.makedirs('favicons', exist_ok=True)
    os.chdir('favicons')
    
    # Process each domain
    for domain in domains:
        domain = domain.strip()
        if domain:
            download_favicon(domain)

# Example usage
domains = """

""".strip().split('\n')

process_domains(domains)
