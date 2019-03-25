# author Matt Bussing
import os
from datetime import datetime, timedelta
from time import sleep

import pytz

from distancepi.my_threads import Repeat


class Device():
    """
    This class couples both the jobs of input from the sensehat or keyboard
    and the display (sensehat or terminal)
    """

    green = (0, 255, 0)
    yellow = (255, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    white = (255, 255, 255)
    nothing = (0, 0, 0)
    pink = (255, 105, 180)

    def __init__(self, verbose=False, test_sleep=False,
                 on_computer=False, tests=False, sleep_on=False):
        self.verbose = verbose
        self.test_sleep = test_sleep
        self.on_computer = on_computer
        self.sleep_on = sleep_on
        self.tests = tests
        self.processes_stopped = True

        if tests:
            print("tests active")

        self.load_config()
        if not self.on_computer:
            from sense_hat import SenseHat
            self.sense_hat = SenseHat()
            self.sense_hat.low_light = True
            self.sense_options()

    def main(self):
        if self.processes_stopped:
            self.update_times()
            self.start_processes()
        # Loops until time for bed then it goes to sleep till morning
        try:
            i = 0
            while True:
                self.update_times()

                # if it is not during the time that someone wants a message
                # displayed, we put it to sleep
                if self.time_to_sleep and self.sleep_on or self.test_sleep:
                    self._sleep()
                # if we come out of sleep it is time to start the processes
                if self.processes_stopped:
                    self.start_processes()

                # this is for testing
                if self.tests:
                    sleep(1)
                    print("next", i)
                    if i > 3:
                        self.stop_processes()
                        return self.message_list
                    i += 1

                else:  # pauses for 30 seconds before restarting loop
                    sleep(30)

        except KeyboardInterrupt:
            print('KeyboardInterrupt received. Exiting.')
            self.stop_processes()
            exit()

    def display_heart(self):
        o = Device.nothing
        p = Device.pink
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

        self.sense_hat.set_pixels(heart)
        sleep(10)

    def display(self):
        for i in self.message_list:
            self.display_helper(i)
        if not self.on_computer:
            self.display_heart()

    def display_helper(self, phrase):
        if self.on_computer:
            print(phrase)
        else:
            self.sense_hat.show_message(phrase)

    def stop_processes(self):
        # TODO: fix threads to make it so that you can pause and continue
        self.processes['print'].stop()
        self.processes['get'].stop()
        if self.verbose:
            print("processes killed")
        if not self.on_computer:
            self.sense_hat.clear()
        self.processes_stopped = True

    def start_processes(self):
        self.processes = {
            'get': Repeat(30, self.get_messages),
            'print': Repeat(3, self.display)
        }
        if self.verbose:
            print("starting processes")
        self.processes['print'].start()
        self.processes['get'].start()
        self.processes_stopped = False

    def shutdown(self):
        self.stop_processes()
        self.display_helper("shutting down")
        os.system('sudo shutdown now')

    def sense_options(self):
        if not self.on_computer:
            def pushed_up(event):
                if event.action != 'released':
                    self.shutdown()

            def pushed_down(event):
                if event.action != 'released':
                    print("pressed down")

            def pushed_left(event):
                if event.action != 'released':
                    print("pressed left")

            def pushed_right(event):
                if event.action != 'released':
                    print("pressed right")

            def refresh():
                self.sense_hat.clear()

            self.sense_hat.stick.direction_up = pushed_up
            self.sense_hat.stick.direction_down = pushed_down
            self.sense_hat.stick.direction_left = pushed_left
            self.sense_hat.stick.direction_right = pushed_right

    def update_times(self):
        temp = datetime.now(tz=pytz.timezone("America/Denver"))

        self.now = temp
        # TODO: ADD THING TO MAKE THE TIME NOT UPDATE EVERYTIME
        new_day = True
        if new_day:
            self.morning = self.now.replace(
                hour=self.morningTime, minute=0, second=0, microsecond=0)
            self.evening = self.now.replace(
                hour=self.eveningTime, minute=0, second=0, microsecond=0)

            # this makes it so that we see everthing from two nights ago on
            self.time_before = self.evening - timedelta(days=2)

        self.time_to_sleep = not(
            self.now < self.evening and self.now > self.morning)

    def _sleep(self):
        """ These are all the things we do when sleeping"""
        self.sense_hat.clear()
        self.stop_processes()

        # find the time to wake up
        time_to_sleep = self._get_time_to_sleep()
        if self.verbose:
            print("going to sleep", time_to_sleep.total_seconds(),
                  time_to_sleep)

        # this is so you can test without waiting forever
        if not self.tests:
            sleep(time_to_sleep.total_seconds())  # sleeps until morning
        else:
            print("testing sleep")
            sleep(0.01)
            print("sleeping for", time_to_sleep.total_seconds(), time_to_sleep)

    def _get_time_to_sleep(self):
        return abs(self.morning - self.now)
