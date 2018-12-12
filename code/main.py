# author Matt Bussing
import json
import os
import re
import sys
from datetime import datetime, time
from time import sleep

import pytz
import requests

from my_threads import MyThread, Repeat


class Device(object):
    def __init__(self, name="main.py", verbose=False, testSleep=False, onComputer=False, tests=False):
        self.verbose = verbose
        self.testSleep = testSleep
        self.onComputer = onComputer
        self.messageList = ["Messages not updated yet"]
        self.name = name
        self.tests = tests
        if tests:
            print("tests active")
        self.location = re.sub(self.name, "", sys.argv[0])

        self.processes = {'get': Repeat(30, self.getMessages), 'print': Repeat(3, self.display), 'options':
                          MyThread(self.senseHatOptions)}

        # loads config file (config)
        try:
            with open(self.location + 'config.json', 'r') as f:
                config = json.load(f)
        except IOError:
            print("error missing config file")
            exit(-1)

        self.morning = time(hour=config['MORNING'])
        self.evening = time(hour=config['EVENING'])
        self.url = config['URL']
        self.client = config['CLIENT']
        self.expiration = config['EXPIRATION']

        if not self.onComputer:
            from sense_hat import SenseHat
            self.senseHat = SenseHat()

        self.processes['print'] = Repeat(3, self.display)

        for i, j in self.processes.items():
            j.start()

    def display(self):
        if self.onComputer:
            displayFunction = print
        else:
            displayFunction = self.senseHat.show_message
        for i in self.messageList:
            displayFunction(i)

    def processEnd(self):
        self.processes['print'].stop()
        self.processes['get'].stop()
        # self.processes['options'].stop()

    def shutdown(self):
        self.processes['print'].stop()
        self.processes['get'].stop()
        # self.processes['options']
        if not self.onComputer:
            self.senseHat.clear()
            self.senseHat.show_message("shutting down")
        else:
            print("shutting down")
        if self.verbose:
            print("processes killed")
        os.system('sudo shutdown now')

    def senseHatOptions(self):
        if not self.onComputer:
            event = self.stick.wait_for_event()
            if verbose:
                print(event)
            if(event.direction == 'up'):
                self.shutdown()

    def getMessages(self):
        if self.verbose:
            print("getting messages")
        r = requests.get(url=self.url + self.client)

        if(r.status_code == 200):
            # emptys the list
            self.messageList = []
            mList = r.json()['messages']
            if not(mList[0] == 'none'):  # checks to see if anything passed
                for i in mList:
                    # returns the json string of date / time as a datetime object with timezone
                    # 2018-08-13T13:35:58.078103
                    postDate = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    postDate = pytz.utc.localize(postDate, is_dst=None)

                    # finds difference between when the item was posted and rn
                    diff = datetime.now(tz=pytz.utc) - postDate

                    if self.verbose:
                        print(diff.total_seconds(), self.expiration)
                    # deletes the message if it is too old and continues
                    if diff.total_seconds() > self.expiration:
                        self.DeleteMessages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    self.messageList.append(i['message'])

        else:
            self.messageList = ["Server not working properly"]

    def DeleteMessages(self, message):
        if self.verbose:
            print("Deleting old message")
        r = requests.delete(url=self.url + self.client,
                            json={'message': message})

        if(r.status_code == 200):
            if self.verbose:
                print(r.json()['message'])
        else:
            self.messageList = ["Server not working properly"]

    def main(self):
        currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
        self.eveningD = datetime(currentDay.year,
                                 currentDay.month,
                                 currentDay.day,
                                 hour=self.evening.hour,
                                 minute=self.evening.minute,
                                 second=self.evening.second,
                                 microsecond=self.evening.microsecond,
                                 tzinfo=pytz.timezone("America/Denver")
                                 )
        # Loops until time for bed then it goes to sleep till morning
        isStopped = False  # flags if the process stops
        try:
            i = 0
            while True:
                currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
                rn = currentDay.time()
                # This checks to see if we want to display messages right now (rn)
                if(not(rn < self.evening and rn > self.morning) and willSleep or self.testSleep):
                    # Stops processes
                    self.processEnd()
                    isStopped = True

                    # this fixes the event that it is past midnight
                    differentDay = 0
                    if currentDay >= eveningD:
                        differentDay = 1

                    morningDate = datetime(currentDay.year,
                                           currentDay.month,
                                           currentDay.day + differentDay,
                                           hour=self.morning.hour,
                                           minute=self.morning.minute,
                                           second=self.morning.second,
                                           microsecond=self.morning.microsecond,
                                           tzinfo=pytz.timezone(
                                               "America/Denver")
                                           )

                    if self.testSleep:
                        sleep(5)
                        self.testSleep = False
                    else:
                        diff = abs(morningDate - currentDay)
                        if verbose:
                            print("going to sleep", diff.total_seconds(), diff)
                        sleep(diff.total_seconds())  # sleeps until morning

                if self.verbose:
                    print("isStopped=")
                    print(isStopped)

                if isStopped:  # checks if processes were killed
                    # restarts processes if time to display
                    if verbose:
                        print("starting processes")
                    processes = self.processStart()
                    isStopped = False  # resets

                if self.tests:
                    sleep(1)
                    print("next", i)
                    if i > 5:
                        self.processEnd()
                        return self.messageList
                    i += 1
                else:
                    sleep(30)  # pauses for 30 seconds before restarting loop
        except KeyboardInterrupt:
            print('KeyboardInterrupt received. Exiting.')
            self.processEnd()
            exit()


if __name__ == '__main__':
    d = Device()
    # processes command line arguments
    for i in sys.argv[1:]:
        if(i == "-l"):  # makes server local
            print('using local server')
            d.config['URL'] = 'http://127.0.0.1:5000'

        elif(i == "-s"):  # This sets up test data
            print('setting sleep variable off')
            d.config['SLEEP'] = False

        elif(i == "-v"):  # makes server local
            print('verbose')
            d.verbose = True

    d.main()
