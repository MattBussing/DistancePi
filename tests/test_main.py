# Author Matt Bussing
# run using py.test tests.py

# import pytest

from distancepi.__main__ import get_args

# from main import get_args


def test_get_args():
    list = ["asdf", "asf", "--config", "file"]
    assert get_args(list) == "file"


# [matt@jackjack DistancePi]$ python3.7 - m distancepi - -config
