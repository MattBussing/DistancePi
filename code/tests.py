# Author Matt Bussing
# run using py.test tests.py
import sys

from main import Device


def test_config_location():
    # d = Device()
    loc = Device.get_config_location("tests")
    assert sys.argv == []
    assert loc == []


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
