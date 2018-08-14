from datetime import datetime

import requests
import pytz


class Messages():
    def __init__(self, url, client, expirationDate):
        # Stores a list of messages
        self.messageList = ["Messages not updated yet"]
        self.url = url
        self.client = client
        self.expirationDate = expirationDate

    def getMessages(self):
        print("getting message")
        r = requests.get(url = self.url + self.client)

        if(r.status_code == 200):
            self.messageList = []

            mList = r.json()['messages']
            if not(mList[0] == 'none'):
                for i in mList:
                    local_tz = pytz.timezone("America/Denver")
                    postDate = datetime.strptime(i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f") #2018-08-13T13:35:58.078103
                    postDate = local_tz.localize(postDate)
                    diff = datetime.now(tz=pytz.utc).astimezone(local_tz) - postDate
                    print(diff.total_seconds() , self.expirationDate)

                    if diff.total_seconds() > self.expirationDate:
                        self.DeleteMessages(i['message'])
                        continue

                    self.messageList.append(i['message'])

        else:
            self.messageList = ["Server not working properly"]

        if len(self.messageList):
            self.messageList = [ 'no new messages' ]

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
