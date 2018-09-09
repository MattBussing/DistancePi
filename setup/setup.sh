# Author: Matt Bussing
# set up ssh and wifi via raspi-config
# for ssh add the file ssh to the boot folder



sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install git
sudo apt-get install python3-pip
# sudo apt-get install vim
cd
if [ ! -d "DistancePi" ]; then
    sudo git clone https://github.com/MattBussing/DistancePi.git
fi

# intstall and update programs
sudo pip3 install -U pip
sudo pip3 install pytz
sudo pip3 install -U pytz
sudo pip3 install requests
sudo pip3 install -U requests


sudo apt-get install sense-hat

#sets up rc.local
cd DistancePi
echo '{
    "DEBUG": false,
    "SLEEP": true,
    "CLIENT":"Matt",
    "URL":"https://distance-pi.herokuapp.com",
    "EXPIRATION": 18000
}' > code/config.json
<<notes

# checks to see if there is a back up for the file
if [ ! -f /etc/rclocalBackup.txt ]; then
    sudo cp /etc/rc.local /etc/rclocalBackup.txt
fi
sudo cp setup/rc.local /etc/rc.local
sudo chmod +x /etc/rc.local

sudo systemctl daemon-reload

sudo reboot

StandardOutput=tty
sudo systemctl status myscript.service
notes
