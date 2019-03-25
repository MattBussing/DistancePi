# Author Matt Bussing


from distancepi.__main__ import get_config_loc


def test_get_config_loc():
    list = ["asdf", "asf", "--config", "file"]
    assert get_config_loc(list) == "file"
