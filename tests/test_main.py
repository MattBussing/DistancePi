# Author Matt Bussing
# run using py.test tests.py

# import pytest

from distancepi.__main__ import get_args

# from main import get_args


def test_get_args():
    list = ["asdf", "asf", "--config", "file"]
    assert get_args(list) == "file"


# [matt@jackjack DistancePi]$ python3.7 - m distancepi - -config

# def test_config_location():
#     # d = Device()
#     loc = Device.get_config_location("tests")
#     assert sys.argv == []
#     assert loc == []


# def test_get_messages():
#     d = Device()
#     d.get_messages
#     print(d.message_list)
#     assert 5 == 5
#
#
# def test_load_config():
#     d = Device._load_config()
#     d._load_config()
