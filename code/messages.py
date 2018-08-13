from datetime import datetime

import requests
import pytz


class Messages():
    def __init__(self, url, client, expirationDate):
        # Stores a list of messages
        self.messageList = ["Message not updated yet"]
        self.url = url
        self.client = client
        self.expirationDate = expirationDate

    def getMessages(self):
        print("getting message")
        r = requests.get(url = self.url + self.client)

        if(r.status_code == 200):
            mList = r.json()['messages']
            if mList[0] == 'none':
                self.messageList = [ 'no new messages' ]
            else:
                self.messageList = []
                for i in mList:
                    lol = datetime.strptime(i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f").astimezone(pytz.timezone("America/Denver")) #2018-08-13T13:35:58.078103
                    diff = datetime.now(tz=pytz.utc).astimezone(pytz.timezone("America/Denver")) - lol
                    if diff.total_seconds() > self.expirationDate:
                        print(diff.total_seconds())
                        self.DeleteMessages(i['message'])
                        continue
                    self.messageList.append(i['message'])
        else:
            self.messageList = ["Server not working properly"]

    def DeleteMessages(self, message):
        print("Deleting old message")
        r = requests.delete(url = self.url + self.client, json = {'message':message})

        if(r.status_code == 200):
            print(r.json()['message'])
        else:
            self.messageList = ["Server not working properly"]

    def display(self, displayFunction):
        for i in self.messageList:
            displayFunction(i)
