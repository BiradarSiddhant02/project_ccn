#!/bin/bash

# Run packet_sniff.py in the background
sudo python3 packet_sniff.py > cap.txt &

# Store the process ID of the background command
PID=$!

# Wait for user input (pressing 'q') to terminate packet_sniff.py
read -n 1 -p "Press 'q' to stop packet_sniff.py: " input

# Check if the user pressed 'q'
if [ "$input" == "q" ]; then
  # Terminate packet_sniff.py
  sudo kill $PID
  echo "packet_sniff.py terminated."
  
  # Run the next command (syn-filter.py)
  python3 syn-filter.py > syn.txt
else
  echo "Invalid input. Exiting without running syn_filter.py."
fi
