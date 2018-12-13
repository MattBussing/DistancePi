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

bash scripts/configSetup.sh

bash linkRC.sh

sudo systemctl daemon-reload
sudo reboot
# sudo systemctl status myscript.service
