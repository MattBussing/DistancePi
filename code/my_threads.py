from threading import Thread, Event


class Repeat(Thread):
    def __init__(self,delay,function,*args,**kwargs):
        Thread.__init__(self)
        self.abort = Event()
        self.delay = delay
        self.args = args
        self.kwargs = kwargs
        self.function = function
    def stop(self):
        self.abort.set()
    def run(self):
        while not self.abort.isSet():
            self.function(*self.args,**self.kwargs)
            self.abort.wait(self.delay)


# TODO: get rid of event
class myThread (Thread):
    def __init__(self,function,*args,**kwargs):
        Thread.__init__(self)
        self.abort = Event()
        self.args = args
        self.kwargs = kwargs
        self.function = function
    def run(self):
        self.function(*self.args,**self.kwargs)
