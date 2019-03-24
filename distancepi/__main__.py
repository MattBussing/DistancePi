# author Matt Bussing
import json
import os
import sys
from datetime import datetime, timedelta
from time import sleep

import pytz
import requests

from distancepi.my_threads import Repeat


class Device(object):
    def __init__(self, verbose=False, test_sleep=False,
                 on_computer=False, tests=False, sleep_on=False):
        self.verbose = verbose
        self.test_sleep = test_sleep
        self.on_computer = on_computer
        self.sleep_on = sleep_on
        self.tests = tests
        self.message_list = ["Messages not updated yet"]
        if tests:
            print("tests active")

        self.load_config()
        if not self.on_computer:
            from sense_hat import SenseHat
            self.sense_hat = SenseHat()
            self.sense_hat.low_light = True

        self.update_times()
        self.start_processes()
        self.sense_options()

    def load_config(self):
        print(sys.argv)
        config_loc = get_args(sys.argv)
        print(sys.argv)
        # loads config file (config)s
        try:
            with open(config_loc, 'r') as f:
                config = json.load(f)
        except IOError:
            print("error missing config file")
            exit(-1)
        self.morningTime = config['MORNING']
        self.eveningTime = config['EVENING']
        self.url = config['URL']
        self.client = config['CLIENT']

    def display(self):
        for i in self.message_list:
            self.display_helper(i)

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
        self.isStopped = True

    def start_processes(self):
        self.processes = {
            'get': Repeat(30, self.get_messages),
            'print': Repeat(3, self.display)
        }
        if self.verbose:
            print("starting processes")
        self.processes['print'].start()
        self.processes['get'].start()
        self.isStopped = False

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

    def get_messages(self):
        if self.verbose:
            print("getting messages")
        r = requests.get(url=self.url + self.client)

        if(r.status_code == 200):
            # emptys the list
            self.message_list = []
            message_list = r.json()['messages']
            # checks to see if anything passed
            if not(message_list[0] == 'none'):
                for i in message_list:
                    # returns the json string of date / time as a datetime
                    # object with timezone
                    # 2018-08-13T13:35:58.078103
                    post_date = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    post_date = pytz.utc.localize(post_date, is_dst=None)

                    if post_date < self.nightBefore:
                        self.delete_messages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    self.message_list.append(i['message'])

        else:
            self.message_list = ["Server not working properly"]

    def delete_messages(self, message):
        if self.verbose:
            print("Deleting old message")
        r = requests.delete(url=self.url + self.client,
                            json={'message': message})

        if(r.status_code == 200):
            if self.verbose:
                print(r.json()['message'])
        else:
            self.message_list = ["Server not working properly"]

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
            self.nightBefore = self.evening - timedelta(days=2)

        self.time_to_sleep = not(
            self.now < self.evening and self.now > self.morning)

    def _sleep(self):
        """ These are all the things we do when sleeping"""
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

    def main(self):
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
                if self.isStopped:
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

    def make_heart(self):
        # green = (0, 255, 0)
        # yellow = (255, 255, 0)
        # blue = (0, 0, 255)
        # red = (255, 0, 0)
        # white = (255, 255, 255)
        nothing = (0, 0, 0)
        pink = (255, 105, 180)
        o = nothing
        p = pink
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


def get_args(list):
    # this handles how we deal with the args passed into the system
    length = len(list)
    config_loc = None
    for i in range(1, length):
        if list[i] == "--config":
            # print(list[i + 1][0:2])
            if length <= i + 1:
                raise IOError("no config file specified")
            elif list[i + 1][0:2] == "--":
                raise IOError("config file cannot start with flag (--)")
            else:
                config_loc = list[i + 1]
    if config_loc is None:
        raise IOError("Must use --config flag")
    return config_loc


def main():
    d = Device(sleep_on=True)
    # d = Device(sleep_on=True, on_computer=True)
    # d.main()
    d.make_heart()


if __name__ == '__main__':
    main()
