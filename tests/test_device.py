# Author Matt Bussing
from time import sleep

from distancepi.__main__ import load_config
from distancepi.device import Device
from distancepi.models import User


def test_sleep_cycle():
    d = Device(user=User(
        load_config("/home/pi/DistancePi/config/test_config.json")))
    d.start_processes()
    sleep(2)
    d.sleep(True)
    d.start_processes()
    sleep(2)
    d.stop_processes()
    # assert heart == goal
