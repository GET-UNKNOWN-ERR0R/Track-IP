#!/bin/bash

# Checking for python3 installed or not
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Checking for libraries are installed
echo "Checking for required libraries..."
python3 -c "import webbrowser, sys, os, json, urllib" 2>/dev/null

if [ $? -ne 0 ]; then
    echo "Required libraries not found. Installing..."
    pip3 install webbrowser sys os json urllib
fi

# Run the Python script
echo "Running IP Address Locator..."
python3 iptracker.py
