# sudo cat /media/matt/rootfs/etc/wpa_supplicant/wpa_supplicant.conf
# echo
# echo 'network={
#     ssid="lol"
#     psk="pswd"
# }' | sudo tee -a  /media/matt/rootfs/etc/wpa_supplicant/wpa_supplicant.conf
# echo
# sudo cat /media/matt/rootfs/etc/wpa_supplicant/wpa_supplicant.conf
sudo cat /media/matt/rootfs/etc/rc.local
echo "##############################"
echo '#!/bin/sh -e
#
# rc.local
#
# run via "sudo bash rc.local"

## By default this script does nothing.
# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
  sudo apt-get install -y git
  cd
  sudo git clone https://github.com/MattBussing/DistancePi.git
  bash DistancePi/setup.sh
  sudo reboot

fi
exit 0
' | sudo tee  /media/matt/rootfs/etc/rc.local
echo "##############################"
sudo cat /media/matt/rootfs/etc/rc.local

make file ssh in boot partition to enable ssh
change password via ssh passwd

sudo apt-get install python3-pip
pip install pytz
