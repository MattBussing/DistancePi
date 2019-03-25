# Author Matt Bussing

from distancepi.model import Model


def test_instantiated_correctly():
    model = Model()
    assert model.message_list == ["Messages not updated yet"]
    assert model.thought_of == 0


def test_changed_correctly():
    model = Model()
    model.message_list = []
    model.thought_of = 22

    assert model.message_list == []
    assert model.thought_of == 22
