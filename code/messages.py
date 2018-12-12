from datetime import datetime

import requests

import pytz


class Messages():
    def __init__(self, url, client, expirationDate, verbose=False):
        # Stores a list of messages
        self.messageList = ["Messages not updated yet"]
        self.url = url
        self.client = client
        self.expirationDate = expirationDate
        self.verbose = verbose

    def getMessages(self):
        if self.verbose:
            print("getting messages")
        r = requests.get(url=self.url + self.client)

        if(r.status_code == 200):
            # emptys the list
            self.messageList = []
            mList = r.json()['messages']
            if not(mList[0] == 'none'):  # checks to see if anything passed
                for i in mList:
                    # returns the json string of date / time as a datetime object with timezone
                    # 2018-08-13T13:35:58.078103
                    postDate = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    postDate = pytz.utc.localize(postDate, is_dst=None)

                    # finds difference between when the item was posted and rn
                    diff = datetime.now(tz=pytz.utc) - postDate

                    if self.verbose:
                        print(diff.total_seconds(), self.expirationDate)
                    # deletes the message if it is too old and continues
                    if diff.total_seconds() > self.expirationDate:
                        self.DeleteMessages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    self.messageList.append(i['message'])

        else:
            self.messageList = ["Server not working properly"]

        # if len(self.messageList) == 0:
        #     self.messageList.append('no new messages')

    def DeleteMessages(self, message):
        if self.verbose:
            print("Deleting old message")
        r = requests.delete(url=self.url + self.client,
                            json={'message': message})

        if(r.status_code == 200):
            if self.verbose:
                print(r.json()['message'])
        else:
            self.messageList = ["Server not working properly"]

    def display(self, displayFunction):
        for i in self.messageList:
            displayFunction(i)
