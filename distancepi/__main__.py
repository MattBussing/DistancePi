# author Matt Bussing
import json
import sys

from distancepi.device import Device
from distancepi.models import User


def get_config_loc(list):
    # this handles how we deal with the args passed into the system
    # right now all it does is return the config location
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


def load_config(config_loc=None):
    if config_loc is None:
        config_loc = get_config_loc(sys.argv)
    # loads config file (config)s
    try:
        with open(config_loc, 'r') as f:
            return json.load(f)
    except IOError:
        print("error missing config file")
        exit(-1)


if __name__ == '__main__':
    d = Device(user=User(load_config()))
    d.main()
