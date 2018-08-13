import requests

class Messages():
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
        for i in self.messageList:
            displayFunction(i)
