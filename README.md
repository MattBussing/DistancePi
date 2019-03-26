# Distance Pi
This project is intended to be ran on a raspberry pi. One can upload content onto the server and the pi pulls and Views the message.

# Instructions
Install via `$(sudo) python3 -m pip install -e . --user`
## Running
- Normal: `python3 -m distancepi --config config/config.json`
- Fun counter: `python3 distancepi/device.py`

# Notes
 - This project assumes you are using a headless raspberry pi with sensehat. If you want to see the messages then run with onComputer=True

## Helpful Commands
- `sudo systemctl daemon-reload`
- `sudo systemctl start DistancePi.service`
- `journalctl -u DistancePi.service`

## Known Issues
- Threads aren't started and stopped properly
- Multiple of the same threads will be started
- Keyboard interupt doesn't work with threads
- If the sensehat it used by more than one thread (or process)
  it prints both at the same time with weird flickering
