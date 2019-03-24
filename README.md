# Distance Pi
This project is intended to be ran on a raspberry pi. One can upload content onto the server and the pi pulls and displays the message.

# Instructions
Install via `$(sudo) python3 -m pip install -e . --user`

#Notes
 - scp documents/DistancePi/code/exampleconfig.json pi@[ip_address]:$HOME/DistancePi/code/config.json to move config to pi
 - This project assumes you are using a headless raspberry pi with sensehat. If you want to see the messages then run with onComputer=True
