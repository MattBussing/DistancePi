import requests
class Messages():
    def __init__(self):
        self.message = "Message not updated yet"

    def updateMessage(self):
        print("getting message")
        r = requests.get(url='https://distance-pi.herokuapp.com/pi/Matt')
        if(r.status_code == 200):
            self.message = r.json()['item']['message']
        else:
            self.message = "Server not working properly"

    def display(self, displayFunction):
        displayFunction(self.message)
