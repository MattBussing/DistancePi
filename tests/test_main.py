# Author Matt Bussing


from distancepi.__main__ import get_args


def test_get_args():
    list = ["asdf", "asf", "--config", "file"]
    assert get_args(list) == "file"
