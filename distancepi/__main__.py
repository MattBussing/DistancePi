# author Matt Bussing
import json
import os
import sys
from datetime import datetime, timedelta
from time import sleep

import pytz

from distancepi.my_threads import Repeat


def get_args(list):
    # this handles how we deal with the args passed into the system
    length = len(list)
    config_loc = None
    for i in range(1, length):
        if list[i] == "--config":
            if length <= i + 1:
                raise IOError("no config file specified")
            elif list[i + 1][0:2] == "--":
                raise IOError("config file cannot start with flag (--)")
            else:
                config_loc = list[i + 1]
    if config_loc is None:
        raise IOError("Must use --config flag")
    return config_loc


def load_config(self):
    config_loc = get_args(sys.argv)
    # loads config file (config)s
    try:
        with open(config_loc, 'r') as f:
            config = json.load(f)
    except IOError:
        print("error missing config file")
        exit(-1)
    self.morningTime = config['MORNING']
    self.eveningTime = config['EVENING']
    self.url = config['URL']
    self.client = config['CLIENT']


def main():
    d = Device(sleep_on=True)
    d.main()

    # debug stuff
    # d = Device(sleep_on=True, on_computer=True)
    # d.display_heart()


if __name__ == '__main__':
    main()
