# author Matt Bussing
from datetime import datetime

import pytz
import requests


class ServerConnector():
    def __init__(self, verbose=False, test_sleep=False,
                 on_computer=False, tests=False, sleep_on=False):
        self.verbose = verbose
        self.test_sleep = test_sleep
        self.on_computer = on_computer
        self.sleep_on = sleep_on
        self.tests = tests
        self.message_list = ["Messages not updated yet"]
        self.processes_stopped = True

        if tests:
            print("tests active")

        self.load_config()
        if not self.on_computer:
            from sense_hat import SenseHat
            self.sense_hat = SenseHat()
            self.sense_hat.low_light = True
            self.sense_options()

    def get_messages(self):
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
