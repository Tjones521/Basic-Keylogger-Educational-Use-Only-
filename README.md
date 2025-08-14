# Basic Keylogger (Educational Use Only)

## Overview
This project is a **safe, local keylogger** built with Python for **cybersecurity learning purposes**.  
It demonstrates how keystrokes can be captured and stored locally.  
**Not for malicious use** — running this on devices without permission is illegal.

## Features
- Logs all keys pressed
- Saves to `key_log.txt`
- Stops logging when ESC is pressed

## Legal Disclaimer
This tool is for educational purposes only. The author is not responsible for misuse.

## Installation
```bash
git clone https://github.com/Tjones521/basic-keylogger.git
cd basic-keylogger
python3 -m venv venv
source venv/bin/activate
pip install pynput
python keylogger.py


