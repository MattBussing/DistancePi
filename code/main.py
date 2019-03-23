# author Matt Bussing
import json
import os
import re
import sys
from datetime import datetime, timedelta
from time import sleep

import requests

import pytz
from my_threads import Repeat


class Device(object):
    def __init__(self, name="main.py", verbose=False, test_sleep=False,
                 on_computer=False, tests=False, sleep_on=False):
        self.verbose = verbose
        self.test_sleep = test_sleep
        self.on_computer = on_computer
        self.sleep_on = sleep_on
        self.tests = tests
        self.messageList = ["Messages not updated yet"]
        if tests:
            print("tests active")

        config_loc = re.sub(
            "code/" + name, "config/config.json", sys.argv[0])
        # loads config file (config)
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

        if not self.on_computer:
            from sense_hat import SenseHat
            self.senseHat = SenseHat()

        self.update_times()
        self.start_processes()
        self.sense_options()

    def display(self):
        for i in self.messageList:
            self.display_helper(i)

    def display_helper(self, phrase):
        if self.on_computer:
            print(phrase)
        else:
            self.senseHat.show_message(phrase)

    def stop_processes(self):
        # TODO: fix threads to make it so that you can pause and continue
        self.processes['print'].stop()
        self.processes['get'].stop()
        if self.verbose:
            print("processes killed")
        if not self.on_computer:
            self.senseHat.clear()
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
                self.senseHat.clear()

            self.senseHat.stick.direction_up = pushed_up
            self.senseHat.stick.direction_down = pushed_down
            self.senseHat.stick.direction_left = pushed_left
            self.senseHat.stick.direction_right = pushed_right

    def get_messages(self):
        if self.verbose:
            print("getting messages")
        r = requests.get(url=self.url + self.client)

        if(r.status_code == 200):
            # emptys the list
            self.messageList = []
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
                    self.messageList.append(i['message'])

        else:
            self.messageList = ["Server not working properly"]

    def delete_messages(self, message):
        if self.verbose:
            print("Deleting old message")
        r = requests.delete(url=self.url + self.client,
                            json={'message': message})

        if(r.status_code == 200):
            if self.verbose:
                print(r.json()['message'])
        else:
            self.messageList = ["Server not working properly"]

    def update_times(self):
        self.now = datetime.now(tz=pytz.timezone("America/Denver"))
        self.morning = self.now.replace(
            hour=self.morningTime, minute=0, second=0, microsecond=0)
        self.evening = self.now.replace(
            hour=self.eveningTime, minute=0, second=0, microsecond=0)

        # this makes it so that we see everthing from two nights ago on
        self.nightBefore = self.evening - timedelta(days=2)

        self.timeToSleep = not(
            self.now < self.evening and self.now > self.morning)

    def main(self):
        # Loops until time for bed then it goes to sleep till morning
        try:
            i = 0
            while True:
                self.update_times()
                # This checks to see if we want to display messages right now
                # (rn)
                if self.timeToSleep and self.sleep_on or self.test_sleep:
                    self.stop_processes()

                    diff = abs(self.morning - self.now)
                    if self.verbose:
                        print("going to sleep", diff.total_seconds(), diff)

                    # this is so you can test without waiting forever
                    if not self.tests:
                        sleep(diff.total_seconds())  # sleeps until morning
                    else:
                        print("testing sleep")
                        sleep(0.01)
                        print("sleeping for", diff.total_seconds(), diff)

                if self.isStopped:
                    self.start_processes()

                if self.tests:
                    sleep(1)
                    print("next", i)
                    if i > 3:
                        self.stop_processes()
                        return self.messageList
                    i += 1
                else:
                    sleep(30)  # pauses for 30 seconds before restarting loop
        except KeyboardInterrupt:
            print('KeyboardInterrupt received. Exiting.')
            self.stop_processes()
            exit()


if __name__ == '__main__':
    d = Device(sleep_on=True)
    # d = Device(sleep_on=True, on_computer=True)
    d.main()
