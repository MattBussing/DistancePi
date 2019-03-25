# author Matt Bussing


class Model():
    """
    This is the data that we are storing for this project.
    - message_list stores the messages we have received.
    - thought_of stores the number of times the other person hit the center
     button to think of us.

     For now we will not put any safety mechanisms on the class
    """

    def __init__(self):
        self.message_list = ["Messages not updated yet"]
        self.thought_of = 0
