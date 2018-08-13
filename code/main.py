# author Matt Bussing
import sys
import os
from time import sleep
from datetime import datetime, time

import pytz

from messages import Messages
from repeat import Repeat



# def printTime(x):
#     print (x.strftime('%I:%M %p'))

def processEnd(x):
    for i in x:
        i.stop()
    if not DEBUG:
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

def main( arg, test=False):
    CLIENT='/Matt'
    URL='https://distance-pi.herokuapp.com'
    # This is the time that we want the pi on
    # TODO make the times part of config file
    morning = time(hour=9)
    evening = time(hour=21)
    expirationDate = 48 * 60 * 60 # hr * min/hr * sec/min
    DEBUG = False

    for i in arg:
        if(i in "-d"):
            DEBUG = True
            # TODO make the name part of config file
            URL='http://127.0.0.1:5000'

    m = Messages(URL, CLIENT, expirationDate )

    # This is the process that updates the messages
    rep = Repeat(30, m.getMessages)
    processes = [rep]
    # This is the process that displays the information
    if DEBUG:
        print("Debug mode")
        rep2 = Repeat(3, m.display, print)
        processes.append(rep2)
    else:
        import sense_hat
        global sense
        sense = sense_hat.SenseHat()
        rep2 = Repeat(3, m.display, sense.show_message)
        processes.append(rep2)
        rep3 = Repeat(3, off, x=processes)
        processes.append(rep3)


    # Starts the processes
    processStart(processes)

    # Loops until time for bed then it goes to sleep till morning
    flag = False # flags if the process stops
    try:
        intTemp = 0
        while True:
            currentDay = datetime.now(tz=pytz.utc).astimezone(pytz.timezone("America/Denver"))
            # ##### testing
            # early = time(hour=8)
            # early = datetime(currentDay.year, currentDay.month, currentDay.day,  hour=early.hour, minute=early.minute, second=early.second, microsecond=early.microsecond).astimezone(pytz.timezone("America/Denver"))
            # currentDay = early
            # eveningD = datetime(currentDay.year, currentDay.month, currentDay.day,  hour=evening.hour, minute=evening.minute, second=evening.second, microsecond=evening.microsecond).astimezone(pytz.timezone("America/Denver"))
            # ######
            rn = currentDay.time()

            if( not(rn < evening and rn > morning)): # This checks to see if we want to display rn
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
                    microsecond=morning.microsecond
                ).astimezone(pytz.timezone("America/Denver"))

                diff = morningDate - currentDay
                print("going to sleep", diff.total_seconds(), diff)
                # waits until morning
                sleep(diff.total_seconds())

            elif(flag): # restarts processes if time to display
                processStart(processes)

            sleep(5)
            if test:
                intTemp += 1

            if intTemp > 5:
                return 'success'

    except KeyboardInterrupt:
        print('KeyboardInterrupt received. Exiting.')
        processEnd(processes)
        exit()


if __name__ == '__main__':
    main(sys.argv[1:])
