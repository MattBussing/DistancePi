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
from my_threads import Repeat, MyThread


def processEnd(x, debug=False, verbose=False):
    for i in x:
        i.stop()
    if not debug:
        global sense
        sense.clear()
    if verbose:
        print("processes killed")

def senseHatOptions(x):
    global sense
    event = sense.stick.wait_for_event()
    if verbose:
        print(event)
    if(event.direction == 'up'):
        processEnd(x)
        sense.show_message("shutting down")
        sense.clear()
        os.system('sudo shutdown -h now')
    # TODO add a method for coming out of sleep here

def processStart(url, client, expiration):
    # This is the process that updates the messages
    m = Messages(url, client, expiration)
    processes = [Repeat(30, m.getMessages)]

    # This is the process that displays the information
    if debug:
        processes.append(Repeat(3, m.display, print))
    else:
        import sense_hat
        global sense
        sense = sense_hat.SenseHat()
        processes.append(Repeat(3, m.display, sense.show_message))
        shutdownSwitch = MyThread(senseHatOptions, processes)
        shutdownSwitch.start()

    # Starts the processes
    for i in processes:
        i.start()
    #links processes
    return processes


def main(willSleep, url, client, debug, expiration, morning, evening, testSleep=False, verbose=False):
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
        tzinfo = pytz.timezone("America/Denver")
    )
    #Start processes
    processes = processStart(url, client, expiration)
    # Loops until time for bed then it goes to sleep till morning
    isStopped = False # flags if the process stops
    try:
        while True:
            currentDay = datetime.now(tz=pytz.timezone("America/Denver"))
            rn = currentDay.time()
            if( not(rn < evening and rn > morning) and willSleep or testSleep): # This checks to see if we want to display messages right now (rn)
                #Stops processes
                processEnd(processes, debug, verbose)
                isStopped = True

                # this fixes the event that it is past midnight
                differentDay = 0
                if currentDay >= eveningD:
                    differentDay =1

                morningDate = datetime(currentDay.year,
                    currentDay.month,
                    currentDay.day+differentDay,
                    hour=morning.hour,
                    minute=morning.minute,
                    second=morning.second,
                    microsecond=morning.microsecond,
                    tzinfo = pytz.timezone("America/Denver")
                )

                if testSleep:
                    sleep(5)
                    testSleep = False
                else:
                    diff = abs(morningDate - currentDay)
                    if verbose:
                        print("going to sleep", diff.total_seconds(), diff)
                    sleep(diff.total_seconds())# sleeps until morning

            if verbose:
                print("isStopped=")
                print(isStopped)

            if isStopped: #checks if processes were killed
                # restarts processes if time to display
                if verbose:
                    print("starting processes")
                processes = processStart(url, client, expiration)
                isStopped = False # resets

            sleep(30)# pauses for 30 seconds before restarting loop

    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Exiting.')
        processEnd(processes,debug)
        exit()

if __name__ == '__main__':
    NAME = "main.py"
    LOCATION = re.sub(NAME, "", sys.argv[0])
    debug = False
    testSleep = False
    verbose = False

    #loads config file (config)
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
            config['URL']='http://127.0.0.1:5000'

        elif(i == "-u"): # This sets up test data
            print('uploading test data')
            messageList = [ 'lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

            def postMessage(postData, url, verbose=False):
                r = requests.post(url=url, json=postData)
                print (r)
                return r

            for i in messageList:
                postProcess = MyThread(postMessage, postData= {'message':i, '_to':'Matt'} )
                postProcess.start()

        elif(i == "-e"): # This sets up test data
            print('setting small expiration date for database entries')
            config['EXPIRATION'] = 5*60

        elif(i == "-s"): # This sets up test data
            print('setting sleep variable off')
            config['SLEEP'] = False

        elif(i == "-t"):  # makes server local
            print('testing sleep')
            testSleep = True

        elif(i == "-v"):  # makes server local
            print('verbose')
            verbose = True
    #starts program
    # def main( sleep, url, client, debug, expiration, morning, evening)
    main(config['SLEEP'], config['URL'], config['CLIENT'], debug, config['EXPIRATION'], config['MORNING'], config['EVENING'], testSleep=testSleep, verbose=verbose)
