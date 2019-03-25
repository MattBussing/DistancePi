# author Matt Bussing
from datetime import datetime, timedelta

from pytz import timezone


class Data():
    """
    This is the data that we are storing for this project.
    - message_list stores the messages we have received.
    - thought_of stores the number of times the other person hit the center
     button to think of us.

     For now we will not put any safety mechanisms on the class
    """

    def __init__(self, m_list=["Messages not updated yet"], thought_of=0):
        self.message_list = m_list
        self.thought_of = thought_of


class User():
    """
    This stores a users preferences such as times it should be on
    """

    def __init__(self, config: dict):
        self.morning_time = config['MORNING']
        self.evening_time = config['EVENING']
        self.url = config['URL']
        self.client = config['CLIENT']


class CurrentTime():
    def __init__(self, user):
        self.user = user
        self._set_vars()

    def _set_vars(self):
        self.now = datetime.now(tz=timezone("America/Denver"))
        self._new_day()

    def _new_day(self):
        self.morning = self.now.replace(
            hour=self.user.morning_time, minute=0, second=0, microsecond=0)
        self.evening = self.now.replace(
            hour=self.user.evening_time, minute=0, second=0, microsecond=0)
        # this makes it so that we see everthing from two nights ago on
        self.time_before = self.evening - timedelta(days=2)

    def _set_time_to_sleep(self):
        self.time_to_sleep = not(
            self.now < self.evening and self.now > self.morning)

    def update_times(self):
        self.now = datetime.now(tz=timezone("America/Denver"))
        # TODO: ADD THING TO MAKE THE TIME NOT UPDATE EVERYTIME
        new_day = True
        if new_day:
            self._new_day()
        self._set_time_to_sleep()

    def get_time_to_sleep(self):
        return abs(self.morning - self.now)
