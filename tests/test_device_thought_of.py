# Author Matt Bussing


from distancepi.view import View


def test_add_thought_of_0():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
    view = View()
    thought_of = 0
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_1():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, o, o, View.green,
    ]
    view = View()

    thought_of = 1
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_2():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, p, o, o, o, View.green,
        o, o, o, o, o, o, o, View.green,
    ]
    view = View()

    thought_of = 2
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_8():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, o, o, View.green,
        o, p, p, o, p, p, o, View.green,
        p, p, p, p, p, p, p, View.green,
        p, p, p, p, p, p, p, View.green,
        o, p, p, p, p, p, o, View.green,
        o, o, p, p, p, o, o, View.green,
        o, o, o, p, o, o, o, View.green,
        o, o, o, o, o, o, o, View.green,
    ]
    view = View()

    thought_of = 8
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_9():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, o, View.yellow, o,
    ]
    view = View()

    thought_of = 9
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_10():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, o, View.yellow, View.yellow,
    ]
    view = View()

    thought_of = 10
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_16():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, p, p, o, p, p, o, View.yellow,
        p, p, p, p, p, p, p, View.yellow,
        p, p, p, p, p, p, p, View.yellow,
        o, p, p, p, p, p, o, View.yellow,
        o, o, p, p, p, o, o, View.yellow,
        o, o, o, p, o, o, o, View.yellow,
        o, o, o, o, o, o, View.yellow, View.yellow,
    ]
    view = View()

    thought_of = 16
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_18():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, View.blue, View.blue, o
    ]
    view = View()

    thought_of = 18
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_63():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

    g = View.orange

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
    view = View()

    thought_of = 63
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_71():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

    g = View.orange

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
    view = View()

    thought_of = 71
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_72():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
    view = View()

    thought_of = 72
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal


def test_add_thought_of_73():
    """
    we want to start in the bottom right and work are way up
    """
    o = View.nothing  # background
    p = View.red  # heart color

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
        o, o, o, o, o, o, o, View.green,
    ]
    view = View()

    thought_of = 73
    heart = view.add_thought_of(heart, thought_of)
    assert heart == goal
