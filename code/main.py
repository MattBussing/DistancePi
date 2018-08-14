# author Matt Bussing
import sys
import os
from time import sleep
from datetime import datetime, time

import pytz
import requests

from messages import Messages
from my_threads import Repeat, myThread

DEBUG = False
CLIENT='/Matt'
URL='http://127.0.0.1:5000'

def processEnd(x):
    for i in x:
        i.stop()
    if DEBUG:
        sense.clear()
    print("processes killed")

def processStart(x):
    try:
        for i in x:
            i.start()
    except KeyboardInterrupt:
        print('Keyboard exception received. Exiting.')
        processEnd(x)
        exit()

def off(x):
    event = sense.stick.wait_for_event()
    print(event)
    if(event.direction == 'up'):
        processEnd(x)
        sense.show_message("shutting down")
        sense.clear()
        os.system('sudo shutdown -h now')

def deleteMessage(m):
    return requests.delete(url=URL+CLIENT, json={'message':m})

def postMessage(postData):
    return requests.post(url=URL, json=postData)


def main( arg, test=False):
    # This is the time that we want the pi on
    # TODO make the times part of config file
    morning = time(hour=9)
    evening = time(hour=21)
    expirationDate = 48 * 60 * 60 # hr * min/hr * sec/min

    for i in arg:
        if(i in "-d"):
            print('Entering Debug mode')
            DEBUG = True

        elif(i in "-l"):  # makes server local
            print('using local server')
            global URL
            URL='http://127.0.0.1:5000'

        elif(i in "-u"): # This sets up test data
            print('uploading test data')
            messageList = [ 'lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
            for i in messageList:
                temp = myThread(postMessage, postData= {'message':i, '_to':'Matt'} )
                temp.start()

        elif(i in "-e"): # This sets up test data
            print('setting small expiration date for database entries')
            expirationDate = 5*60


    m = Messages(URL, CLIENT, expirationDate )

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
        rep3 = Repeat(3, off, processes)
        processes.append(rep3)


    # Starts the processes
    processStart(processes)

    # Loops until time for bed then it goes to sleep till morning
    flag = False # flags if the process stops
    try:
        intTemp = 0
        while True:
            currentDay = datetime.now(tz=pytz.utc).astimezone(pytz.timezone("America/Denver"))
            rn = currentDay.time()

            if( not(rn < evening and rn > morning)): # This checks to see if we want to display rn
                # Stops processes
                processEnd(processes)
                flag = True # sets flag

                temp = 0
                if currentDay >= evening:
                    temp =1

                morningDate = datetime(currentDay.year,
                    currentDay.month,
                    currentDay.day+temp,
                    hour=morning.hour,
                    minute=morning.minute,
                    second=morning.second,
                    microsecond=morning.microsecond
                ).astimezone(pytz.timezone("America/Denver"))

                diff = morningDate - currentDay
                print("going to sleep", diff.total_seconds(), diff)
                # waits until morning
                sleep(diff.total_seconds())

            elif(flag): # restarts processes if time to display
                processStart(processes)

    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Exiting.')
        processEnd(processes)
        exit()


if __name__ == '__main__':
    main(sys.argv[1:])
