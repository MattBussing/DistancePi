# https://www.raspberrypi-spy.co.uk/2015/10/how-to-autorun-a-python-script-on-boot-using-systemd/

sudo ln -sf $HOME/DistancePi/config/DistancePi.service /lib/systemd/system/
sudo chmod 644 /lib/systemd/system/DistancePi.service
sudo systemctl daemon-reload
sudo systemctl enable DistancePi.service
# sudo systemctl status myscript.service
# systemctl list-unit-files
