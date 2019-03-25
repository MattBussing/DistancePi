class View():
    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255, 255, 255)
    pink = (255, 105, 180)
    purple = (128, 0, 128)
    orange = (255, 165, 0)
    colors = [green, yellow, blue, red, white, pink, purple, orange]
    nothing = (0, 0, 0)

    def heart(self, thought_of):
        o = View.nothing  # background
        p = View.red  # heart color
        # 8 x 8 pixel array
        heart = [
            o, o, o, o, o, o, o, o,
            o, p, p, o, p, p, o, o,
            p, p, p, p, p, p, p, o,
            p, p, p, p, p, p, p, o,
            o, p, p, p, p, p, o, o,
            o, o, p, p, p, o, o, o,
            o, o, o, p, o, o, o, o,
            o, o, o, o, o, o, o, o
        ]
        self.add_thought_of(heart, thought_of)
        return heart

    def add_thought_of(self, heart: list, thought_of):
        """
        we want to start in the bottom right and work are way up
                    # r * c
                    # r*width + c
        It looks like this:
        thought_of = 0
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, o,
        thought_of = 1
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, o, g,
        thought_of = 2
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, g,
        o, o, o, o, o, o, o, g,
        and so on
        thus 7*7+7 = 1 (0)
             6*7 +7 = 2 (0,1)
        thought_of = 9
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, y, o,
        thought_of = 10
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, o, y, y,
        thought_of = 18
        o, o, o, o, o, o, o, o,
        o, p, p, o, p, p, o, o,
        p, p, p, p, p, p, p, o,
        p, p, p, p, p, p, p, o,
        o, p, p, p, p, p, o, o,
        o, o, p, p, p, o, o, o,
        o, o, o, p, o, o, o, o,
        o, o, o, o, o, b, b, o,
        thus 8*7+6 = 1 (0)
             8*7 +5 = 2 (0,1)
                8*7 +7 -i= (63 -i, 63)

         what about at a really large number?

        """
        thought_of = thought_of % 72
        counter_color = View.colors[int(
            thought_of / 9) % len(self.colors)]
        for i in range(0, thought_of % 9):
            heart[8 * (7 - i) + 7] = counter_color

        for i in range(63 - int(thought_of / 9), 63):
            heart[i] = counter_color
        return heart
