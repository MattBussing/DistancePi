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
    def __init__(self, url, client, expirationDate, verbose=False, testSleep=False):
        self.onComputer = True
        self.messageList = ["Messages not updated yet"]
        self.url = url
        self.client = client
        self.expirationDate = expirationDate
        self.verbose = verbose
        self.testSleep = testSleep

        self.processes = {'get': Repeat(30, self.getMessages), 'print': Repeat(3, self.display), 'options':
                          MyThread(self.senseHatOptions)}

        if self.onComputer:
            pass
        else:
            import sense_hat
            self.senseHat = sense_hat.SenseHat()
            self.processes['print'] = Repeat(3, m.display, sense.show_message)

        for i, j in self.processes.items():
            j.start()

    def processEnd(self):
        self.processes['print'].stop()
        self.processes['get'].stop()
        self.processes['options'].stop()

    def shutdown(self):
        self.processes['print'].stop()
        self.processes['get'].stop()
        # self.processes['options']
        if not self.onComputer:
            self.sense.clear()
            sense.show_message("shutting down")
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
                        print(diff.total_seconds(), self.expirationDate)
                    # deletes the message if it is too old and continues
                    if diff.total_seconds() > self.expirationDate:
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

    def display(self):
        if self.onComputer:
            displayFunction = print
        else:
            displayFunction = sense.show_message
        for i in self.messageList:
            displayFunction(i)

    def main(self, morning, evening):
        morning = time(hour=morning)
        evening = time(hour=evening)
        currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
        eveningD = datetime(currentDay.year,
                            currentDay.month,
                            currentDay.day,
                            hour=evening.hour,
                            minute=evening.minute,
                            second=evening.second,
                            microsecond=evening.microsecond,
                            tzinfo=pytz.timezone("America/Denver")
                            )
        # Loops until time for bed then it goes to sleep till morning
        isStopped = False  # flags if the process stops
        try:
            while True:
                currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
                rn = currentDay.time()
                # This checks to see if we want to display messages right now (rn)
                if(not(rn < evening and rn > morning) and willSleep or self.testSleep):
                    # Stops processes
                    processEnd(processes, debug, verbose)
                    isStopped = True

                    # this fixes the event that it is past midnight
                    differentDay = 0
                    if currentDay >= eveningD:
                        differentDay = 1

                    morningDate = datetime(currentDay.year,
                                           currentDay.month,
                                           currentDay.day + differentDay,
                                           hour=morning.hour,
                                           minute=morning.minute,
                                           second=morning.second,
                                           microsecond=morning.microsecond,
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

                if verbose:
                    print("isStopped=")
                    print(isStopped)

                if isStopped:  # checks if processes were killed
                    # restarts processes if time to display
                    if verbose:
                        print("starting processes")
                    processes = processStart(url, client, expiration)
                    isStopped = False  # resets

                sleep(30)  # pauses for 30 seconds before restarting loop

        except KeyboardInterrupt:
            print('KeyboardInterrupt received. Exiting.')
            self.processEnd()
            exit()


if __name__ == '__main__':
    NAME = "main.py"
    LOCATION = re.sub(NAME, "", sys.argv[0])
    debug = False
    verbose = False

    # loads config file (config)
    try:
        with open(LOCATION + 'config.json', 'r') as f:
            config = json.load(f)
    except IOError:
        print("error missing config file")
        exit(-1)

    # processes command line arguments
    for i in sys.argv[1:]:
        if(i == "-d"):
            print('Entering Debug mode')
            debug = True

        elif(i == "-l"):  # makes server local
            print('using local server')
            config['URL'] = 'http://127.0.0.1:5000'

        elif(i == "-u"):  # This sets up test data
            print('uploading test data')
            messageList = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

            def postMessage(postData, url, verbose=False):
                r = requests.post(url=url, json=postData)
                print(r)
                return r

            for i in messageList:
                postProcess = MyThread(postMessage, postData={
                                       'message': i, '_to': 'Matt'})
                postProcess.start()

        elif(i == "-e"):  # This sets up test data
            print('setting small expiration date for database entries')
            config['EXPIRATION'] = 5 * 60

        elif(i == "-s"):  # This sets up test data
            print('setting sleep variable off')
            config['SLEEP'] = False

        elif(i == "-v"):  # makes server local
            print('verbose')
            verbose = True
    # starts program
    d = Device(config['URL'], config['CLIENT'],
               config['EXPIRATION'], verbose=False)
    d.main(config['MORNING'], config['EVENING'])
