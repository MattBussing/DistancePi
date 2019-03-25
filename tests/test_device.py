# Author Matt Bussing


from distancepi.device import Device


def test_add_thought_of_0():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    heart = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    goal = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    d = Device()
    d.model.thought_of = 0
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_1():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    heart = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    goal = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, Device.green,
    ]
    d = Device()
    d.model.thought_of = 1
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_2():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    heart = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    goal = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, Device.green,
        o, o, o, o, o, o, o, Device.green,
    ]
    d = Device()
    d.model.thought_of = 2
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_8():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    heart = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    goal = [
        o, o, o, o, o, o, o, Device.green,
        o, p, p, o, p, p, o, Device.green,
        p, p, p, p, p, p, p, Device.green,
        p, p, p, p, p, p, p, Device.green,
        o, p, p, p, p, p, o, Device.green,
        o, o, p, p, p, o, o, Device.green,
        o, o, o, p, o, o, o, Device.green,
        o, o, o, o, o, o, o, Device.green,
    ]
    d = Device()
    d.model.thought_of = 8
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_9():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    heart = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
    ]
    goal = [
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, Device.yellow,
    ]
    d = Device()
    d.model.thought_of = 9
    heart = d.add_thought_of(heart)
    assert heart == goal
