#!/bin/bash

# Function to check if connected to WiFi
check_wifi_connection() {
  if iwconfig 2>/dev/null | grep -q "ESSID:"; then
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
    for network in $known_networks; do
      echo "Trying to connect to $network"
      nmcli connection up "$network"
      
      # Check if connection was successful
      if check_wifi_connection; then
        echo "Successfully connected to $network"
        break
      else
        echo "Failed to connect to $network"
      fi
    done
  else
    echo "Already connected to WiFi"
  fi
  
  # Wait before checking again
  sleep 30
done