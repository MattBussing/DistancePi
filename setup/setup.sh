# Author: Matt Bussing
# set up ssh and wifi via raspi-config
# for ssh add the file ssh to the boot folder

# setup crontab with update.sh

#install programs
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install git -y
sudo apt-get install python3-pip -y
sudo apt-get install vim -y
sudo apt-get install sense-hat -y

# gets repo
cd
if [ ! -d "DistancePi" ]; then
    sudo git clone https://github.com/MattBussing/DistancePi.git
fi

SCRIPTS=$HOME/DistancePi/setup/scripts
# intstall and update programs
bash $SCRIPTS/update.sh

bash $SCRIPTS/configSetup.sh

bash $SCRIPTS/linkRC.sh

bash $SCRIPTS/daemonsetup.sh

sudo reboot
