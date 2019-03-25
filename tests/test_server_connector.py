# Author Matt Bussing

from distancepi.server_connector import ServerConnector


def test_instantiated_correctly():
    sc = ServerConnector("https://distance-pi.herokuapp.com",  "/test")
