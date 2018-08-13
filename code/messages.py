import pytz, requests
from datetime import datetime, time

class Messages():
    morning = time(hour=9)
    evening = time(hour=21)
    def __init__(self, url):
        # Stores a list of messages
        self.messageList = ["Message not updated yet"]
        self.url = url

    def getMessages(self):
        print("getting message")
        r = requests.get(url = self.url)

        if(r.status_code == 200):
            mList = r.json()['messages']
            if mList[0] == 'none':
                self.messageList = [ 'no new messages' ]
            else:
                self.messageList = [ i['message'] for i in mList ]
        else:
            self.messageList = ["Server not working properly"]

    def display(self, displayFunction):
        rn = datetime.now(tz=pytz.utc).astimezone(pytz.timezone("America/Denver")).time()
        if(rn < evening and rn > morning):
            displayFunction("time for bed")
        for i in self.messageList:
            displayFunction(i)
