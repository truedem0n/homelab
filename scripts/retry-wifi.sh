#!/bin/bash

# Function to check if connected to WiFi
check_wifi_connection() {
  if iwconfig 2>/dev/null | grep -i 'ESSID:"uper"'; then
    return 0 # Connected
  else
    return 1 # Not connected
  fi
}

# Main loop
while true; do
  if ! check_wifi_connection; then
    echo "Not connected to WiFi. Attempting to connect..."
    
    # Get list of known networks
    known_networks=$(nmcli -t -f NAME connection show)
    
    # Try connecting to each known network
    echo "Trying to connect to uper"
    nmcli connection up "uper"
      
      # Check if connection was successful
    if check_wifi_connection; then
      echo "Successfully connected to uper"
    else
      echo "Failed to connect to uper"
    fi
  else
    echo "Already connected to WiFi"
  fi
  
  # Wait before checking again
  sleep 30
done