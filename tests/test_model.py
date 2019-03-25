# Author Matt Bussing

from distancepi.models import Data


def test_instantiated_correctly():
    data = Data()
    assert data.message_list == ["Messages not updated yet"]
    assert data.thought_of == 0


def test_changed_correctly():
    data = Data()
    data.message_list = []
    data.thought_of = 22

    assert data.message_list == []
    assert data.thought_of == 22
