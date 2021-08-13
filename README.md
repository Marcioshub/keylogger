# Keylogger - Python/Nodejs

Keylogger that saves to a log file and sends it to a remote server. The
keylogger is written in python and the server is written in nodejs.

## Installation

Install nodejs dependencies

```bash
npm install
```

Install the python dependencies

```bash
cd keylogger
pip3 install -r requirements.txt
```

## Usage

```bash
# Start nodejs server
node index.js

# This will start listening for key presses
python3 keylogger.py
```

## Caveats
1. The keylogger.py file was converted to a .exe file and tested on a Windows 10 computer.
2. Depending on your security settings Windows may automatically delete the keylogger file. For testing you may need to modify security settings.
3. By default the server is on port 5000, but you can change it to any ip address or a server
outside the network.
4. The keylogs.txt file will be named with the current date at the front: YYYY-MM-DD-keylogs.txt