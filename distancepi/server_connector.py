# author Matt Bussing
from datetime import datetime

import pytz
import requests


class ServerConnector():
    """
    This is the class we will use to connect the device to the server
    """

    def __init__(self, url: str, client: str):
        self.url = url
        self.client = client

    def get_messages(self):
        r = requests.get(url=self.url + self.client)

        if(r.status_code == 200):
            # emptys the list
            self.message_list = []
            message_list = r.json()['messages']
            # checks to see if anything passed
            if not(message_list[0] == 'none'):
                for i in message_list:
                    # returns the json string of date / time as a datetime
                    # object with timezone
                    # 2018-08-13T13:35:58.078103
                    post_date = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    post_date = pytz.utc.localize(post_date, is_dst=None)

                    if post_date < self.nightBefore:
                        self._delete_messages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    self.message_list.append(i['message'])

        else:
            self.message_list = ["Server not working properly"]

    def _delete_messages(self, message):
        if self.verbose:
            print("Deleting old message")
        r = requests.delete(url=self.url + self.client,
                            json={'message': message})

        if(r.status_code == 200):
            if self.verbose:
                print(r.json()['message'])
        else:
            self.message_list = ["Server not working properly"]
