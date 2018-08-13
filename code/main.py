# author Matt Bussing
from time import sleep
from messages import Messages
from repeat import Repeat
import sys, pytz
from datetime import datetime, time


def processStart(x, y):
    try:
        x.start()
        y.start()
    except KeyboardInterrupt:
        print('Keyboard exception received. Exiting.')
        exit()

if __name__ == '__main__':
    URL='https://distance-pi.herokuapp.com/Matt'
    morning = time(hour=9)
    evening = time(hour=21)
    debug = False

    for i in sys.argv[1:]:
        if(i in "-d"):
            debug = True
            # URL='http://127.0.0.1:5000/Matt'

    m = Messages(URL)

    # This is the process that updates the messages
    rep = Repeat(30, m.getMessages)

    # This is the process that displays the information
    if debug:
        print("debug mode")
        rep2 = Repeat(3, m.display, print)
    else:
        import sense_hat
        global sense
        sense = sense_hat.SenseHat()
        rep2 = Repeat(3, m.display, sense.show_message)

    # Starts the processes
    processStart(rep, rep2)

    # Loops until time for bed then it goes to sleep till morning
    flag = False # flags if the process stops
    while True:
        rn = datetime.now(tz=pytz.utc).astimezone(pytz.timezone("America/Denver")).time()
        bedTime = not(rn < evening and rn > morning)
        print(bedTime)
        if(bedTime):
            # Stops processes
            rep.stop()
            rep.join()
            rep2.stop()
            rep2.join()
            print("processes killed")
            flag = True # sets flag
            # waits 30 min
            sleep(30*60)

            if debug:
                sense.clear()

        elif(flag): # restarts processes if time to display
            processStart(rep, rep2)

        sleep(5)

# def printTime(x):
#     print (x.strftime('%I:%M %p'))
