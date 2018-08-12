# author Matt Bussing
from time import sleep
from messages import Messages
from repeat import Repeat
import sys

if __name__ == '__main__':
    debug = False
    for i in sys.argv[1:]:
        if(i in "-d"):
            debug = True

    m = Messages()
    rep = Repeat(30, m.updateMessage)
    if debug:
        print("debug mode")
        rep2 = Repeat(3, m.display, print)
    else:
        import sense_hat
        sense = sense_hat.SenseHat()
        rep2 = Repeat(3, m.display, sense.show_message)

    # Starts processes
    rep.start()
    rep2.start()
    x = input("Hit enter to stop\n")

    # Stops processes
    rep.stop()
    rep.join()
    rep2.stop()
    rep2.join()
