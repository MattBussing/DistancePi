echo "linking the rc.local file"

# checks to see if there is a back up for the file
if [ ! -f /etc/rclocalBackup.txt ]; then
    sudo cp /etc/rc.local /etc/rclocalBackup.txt
fi

sudo ln -sf /home/pi/DistancePi/setup/rc.local rc.local
sudo chmod 777 /etc/rc.local
