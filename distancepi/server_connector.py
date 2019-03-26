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

    def get_data(self, time_before=None):
        r = requests.get(url=self.url + self.client)
        message_list = list()

        if(r.status_code == 200):
            data = r.json()
            count = data['count']

            # emptys the list
            unparsed_message_list = data['messages']
            # checks to see if anything passed
            if not(unparsed_message_list is None):
                # here it deletes old messages and adds the new
                for i in unparsed_message_list:
                    # returns the json string of date / time as a datetime
                    # object with timezone
                    # 2018-08-13T13:35:58.078103
                    post_date = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    post_date = pytz.utc.localize(post_date, is_dst=None)

                    #  if time befoe is None we just add it to the list
                    if time_before is not None and post_date < time_before:
                        self._delete_messages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    message_list.append(i['message'])

        else:
            message_list = ["Server not working properly"]
        return message_list, count

    def get_messages(self, time_before=None):
        r = requests.get(url=self.url + self.client)
        message_list = list()

        if(r.status_code == 200):
            # emptys the list
            unparsed_message_list = r.json()['messages']
            # checks to see if anything passed
            if not(unparsed_message_list[0] == 'none'):
                # here it deletes old messages and adds the new
                for i in unparsed_message_list:
                    # returns the json string of date / time as a datetime
                    # object with timezone
                    # 2018-08-13T13:35:58.078103
                    post_date = datetime.strptime(
                        i['dateTime'], "%Y-%m-%dT%H:%M:%S.%f")
                    post_date = pytz.utc.localize(post_date, is_dst=None)

                    #  if time befoe is None we just add it to the list
                    if time_before is not None and post_date < time_before:
                        self._delete_messages(i['message'])
                        continue

                    # if it's not deleted, the message is added to the list
                    message_list.append(i['message'])

        else:
            message_list = ["Server not working properly"]
        return message_list

    def _delete_messages(self, message):
        requests.delete(url=self.url + self.client, json={'message': message})
