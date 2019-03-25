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
        o, o, o, o, o, o, Device.yellow, o,
    ]
    d = Device()
    d.model.thought_of = 9
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_10():
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
        o, o, o, o, o, o, Device.yellow, Device.yellow,
    ]
    d = Device()
    d.model.thought_of = 10
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_16():
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
        o, p, p, o, p, p, o, Device.yellow,
        p, p, p, p, p, p, p, Device.yellow,
        p, p, p, p, p, p, p, Device.yellow,
        o, p, p, p, p, p, o, Device.yellow,
        o, o, p, p, p, o, o, Device.yellow,
        o, o, o, p, o, o, o, Device.yellow,
        o, o, o, o, o, o, Device.yellow, Device.yellow,
    ]
    d = Device()
    d.model.thought_of = 16
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_18():
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
        o, o, o, o, o, Device.blue, Device.blue, o
    ]
    d = Device()
    d.model.thought_of = 18
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_63():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    g = Device.orange

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
        g, g, g, g, g, g, g, o
    ]
    d = Device()
    d.model.thought_of = 63
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_71():
    """
    we want to start in the bottom right and work are way up
    """
    o = Device.nothing  # background
    p = Device.red  # heart color

    g = Device.orange

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
        o, o, o, o, o, o, o, g,
        o, p, p, o, p, p, o, g,
        p, p, p, p, p, p, p, g,
        p, p, p, p, p, p, p, g,
        o, p, p, p, p, p, o, g,
        o, o, p, p, p, o, o, g,
        o, o, o, p, o, o, o, g,
        g, g, g, g, g, g, g, g
    ]
    d = Device()
    d.model.thought_of = 71
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_72():
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
    d.model.thought_of = 72
    heart = d.add_thought_of(heart)
    assert heart == goal


def test_add_thought_of_73():
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
    d.model.thought_of = 73
    heart = d.add_thought_of(heart)
    assert heart == goal
