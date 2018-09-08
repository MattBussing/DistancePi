# author Matt Bussing
import sys
import os
from time import sleep
from datetime import datetime, time
import json
import re

import pytz
import requests

from messages import Messages
from my_threads import Repeat, myThread

NAME = "main.py"
LOCATION = re.sub(NAME, "", sys.argv[0])

try:
    with open(LOCATION + 'config.json', 'r') as f:
         config = json.load(f)
except IOError:
    exit(-1)

DEBUG = False
SLEEP = config['SLEEP']
CLIENT = config['CLIENT']
URL = config['URL']
EXPIRTATION = config['EXPIRATION']
MORNING = config['MORNING']
EVENING = config['EVENING']

def processEnd(x):
    for i in x:
        i.stop()
    if not DEBUG:
        global sense
        sense.clear()
    print("processes killed")

def processStart(x):
    for i in x:
        i.start()

def off(x):
    global sense
    event = sense.stick.wait_for_event()
    print(event)
    if(event.direction == 'up'):
        processEnd(x)
        sense.show_message("shutting down")
        sense.clear()
        os.system('sudo shutdown -h now')

def deleteMessage(m):
    global CLIENT
    global URL
    return requests.delete(url=URL+CLIENT, json={'message':m})

def postMessage(postData):
    global URL
    r = requests.post(url=URL, json=postData)
    print (r)
    return r

def main( arg, test=False):
    global SLEEP
    global URL
    global CLIENT
    global DEBUG
    global EXPIRATION
    global MORNING
    global EVENING
    morning = time(hour=9)
    evening = time(hour=21)
    currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
    eveningD = datetime(currentDay.year,
        currentDay.month,
        currentDay.day,
        hour=evening.hour,
        minute=evening.minute,
        second=evening.second,
        microsecond=evening.microsecond,
        tzinfo = pytz.timezone("America/Denver")
    )

    for i in arg:
        if(i == "-d"):
            print('Entering Debug mode')
            DEBUG = True

        elif(i == "-l"):  # makes server local
            print('using local server')
            URL='http://127.0.0.1:5000'

        elif(i == "-u"): # This sets up test data
            print('uploading test data')
            messageList = [ 'lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
            for i in messageList:
                postProcess = myThread(postMessage, postData= {'message':i, '_to':'Matt'} )
                postProcess.start()

        elif(i == "-e"): # This sets up test data
            print('setting small expiration date for database entries')
            EXPIRATION = 5*60

        elif(i == "-s"): # This sets up test data
            print('setting sleep variable off')
            SLEEP = False

    m = Messages(URL, CLIENT, EXPIRTATION )

    # This is the process that updates the messages
    rep = Repeat(30, m.getMessages)
    processes = [rep]
    # This is the process that displays the information
    if DEBUG:
        rep2 = Repeat(3, m.display, print)
        processes.append(rep2)
    else:
        import sense_hat
        global sense
        sense = sense_hat.SenseHat()
        rep2 = Repeat(3, m.display, sense.show_message)
        processes.append(rep2)
        shutdownProcess = myThread(off, processes)
        shutdownProcess.start()

    # Starts the processes
    processStart(processes)

    # Loops until time for bed then it goes to sleep till morning
    flag = False # flags if the process stops
    try:
        while True:
            currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
            # ##### testing
            # early = time(hour=8)
            # early = datetime(currentDay.year, currentDay.month, currentDay.day,  hour=early.hour, minute=early.minute, second=early.second, microsecond=early.microsecond).astimezone(pytz.timezone("America/Denver"))
            # currentDay = early
            # ######
            rn = currentDay.time()
            if( not(rn < evening and rn > morning) and SLEEP): # This checks to see if we want to display rn
                # Stops processes
                processEnd(processes)
                flag = True # sets flag

                temp = 0
                if currentDay >= eveningD:
                    temp =1

                morningDate = datetime(currentDay.year,
                    currentDay.month,
                    currentDay.day+temp,
                    hour=morning.hour,
                    minute=morning.minute,
                    second=morning.second,
                    microsecond=morning.microsecond,
                    tzinfo = pytz.timezone("America/Denver")
                )

                diff = morningDate - currentDay
                print("going to sleep", diff.total_seconds(), diff)
                # waits until morning
                sleep(diff.total_seconds())

            elif(flag): # restarts processes if time to display
                processStart(processes)

            sleep(5)# pauses for 5 seconds

    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Exiting.')
        processEnd(processes)
        exit()


if __name__ == '__main__':
    main(sys.argv[1:])
