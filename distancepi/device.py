# author Matt Bussing
import os
from time import sleep

from distancepi.custom_threads import RepeatedFunction
from distancepi.models import CurrentTime, Data
from distancepi.server_connector import ServerConnector
from distancepi.view import View


class Device():
    """
    This class represents the pi and sense_hat and deal with all the logic of
    the program.
    """

    def __init__(self, user, on_computer=False, sleep_on=False):
        self.model = Data()
        self.user = user
        self.time = CurrentTime(user)
        self.sc = ServerConnector(user.url, user.client)
        self.view = View()
        self.on_computer = on_computer
        self.processes_stopped = True
        self.sleep_on = sleep_on
        self.display_busy = False

        if not self.on_computer:
            from sense_hat import SenseHat
            self.sense_hat = SenseHat()
            self.sense_hat.low_light = True
            self.sense_options()

    def main(self):
        if self.processes_stopped:
            self.start_processes()
        # Loops until time for bed then it goes to sleep till morning
        try:
            # i = 0
            while True:
                self.time.update_times()
                # if it is not during the time that someone wants a message
                # displayed, we put it to sleep
                if self.time.time_to_sleep and self.sleep_on:
                    self._sleep()
                # if we come out of sleep it is time to start the processes
                if self.processes_stopped:
                    self.start_processes()
                sleep(30)
        except KeyboardInterrupt:
            print('KeyboardInterrupt received. Exiting.')
            self.stop_processes()
            exit()

    def display(self):
        for i in self.model.message_list:
            self.display_helper(i)
        if not self.on_computer:
            heart = self.view.heart(self.model.thought_of)
            self.sense_hat.set_pixels(heart)
            sleep(5)

    def display_helper(self, phrase):
        while self.display_busy:
            sleep(5)
        self.display_busy = True
        if self.on_computer:
            print(phrase)
        else:
            self.sense_hat.show_message(phrase)
        self.display_busy = False

    def stop_processes(self):
        # TODO: fix threads to make it so that you can pause and continue
        self.processes['print'].stop()
        self.processes['get'].stop()
        if not self.on_computer:
            self.sense_hat.clear()
        self.processes_stopped = True

    def start_processes(self):
        self.processes = {
            'get': RepeatedFunction(30, self.get_messages),
            'print': RepeatedFunction(3, self.display)
        }
        self.processes['print'].start()
        self.processes['get'].start()
        self.processes_stopped = False

    def shutdown(self):
        self.stop_processes()
        self.display_helper("shutting down")
        os.system('sudo shutdown now')

    def sense_options(self):
        if not self.on_computer:
            def pushed_up(event):
                if event.action != 'released':
                    print("pressed up")
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
                self.sense_hat.clear()

            self.sense_hat.stick.direction_up = pushed_up
            self.sense_hat.stick.direction_down = pushed_down
            self.sense_hat.stick.direction_left = pushed_left
            self.sense_hat.stick.direction_right = pushed_right

    def get_messages(self):
        self.model.message_list = self.sc.get_messages()

    def sleep(self, testing=False):
        """ These are all the things we do when sleeping"""
        self.sense_hat.clear()
        self.stop_processes()

        # find the time to sleep
        time_to_sleep = self.time.get_time_to_sleep()
        # this is so you can test without waiting forever
        if not testing:
            sleep(time_to_sleep.total_seconds())  # sleeps until morning
        else:
            print("testing sleep")
            sleep(0.01)
            print("sleeping for", time_to_sleep.total_seconds(), time_to_sleep)


if __name__ == "__main__":
    d = Device()
    while True:
        d.View_heart()
        d.model.thought_of += 1
        sleep(2)
