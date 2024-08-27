Overview
"PINNG" is a tool designed to check and report on your internet connection's speed, connectivity, and packet loss. 
It's a simple yet effective utility for diagnosing network issues and ensuring that your internet connection is performing as expected.
Features

    Internet Speed: Measures and reports your download and upload speeds.
    Connectivity Status: Checks if you are connected to the internet.
    Packet Loss: Monitors and reports packet loss during network communication.

Installation

To use the Internet Status Monitor, you need to have Python installed on your system.

git clone https://github.com/yourusername/internet-status-monitor.git

Navigate to the project directory:

cd internet-status-monitor

(Optional) Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

    pip install -r requirements.txt

Usage

To run the Internet Status Monitor, execute the following command:
python monitor.py

The script will output the current status of your internet connection, including speed, connectivity, and packet loss.
Configuration

You can configure the script to adjust the frequency of checks or other parameters by editing the config.json file. Refer to the comments in the file for details on each configurable option.
