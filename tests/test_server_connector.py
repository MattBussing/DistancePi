# Author Matt Bussing
from datetime import datetime, timedelta
from time import sleep

import pytz
import requests

from distancepi.server_connector import ServerConnector

url = "https://distance-pi.herokuapp.com"
test = "test"
client = "/" + test
client_url = url + client
del_url = client_url
post_url = url + "/"
del_json = {'message': 'value'}
post_json = {'message': 'value', '_to': 'testing'}

main_message_list = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

messages_deleted = False


def clean_up(need_to: bool = False):
    global messages_deleted
    if not messages_deleted or need_to:
        messages_deleted = True
        _delete_all_messages()
        for i in main_message_list:
            _post_message(post_data={'message': i, '_to': test})


def _delete_message(del_data):
    requests.delete(url=del_url, json=del_data)


def _post_message(post_data):
    return requests.post(url=post_url, json=post_data)


def _get_all_messages():
    req_data = requests.get(url=client_url)
    message_list = []
    if(req_data.status_code == 200):
        message_list = req_data.json()['messages']
    return message_list


def _delete_all_messages():
    messages = _get_all_messages()
    for i in messages:
        _delete_message({'message': i})


def test_get_messages():
    clean_up()
    sc = ServerConnector(url, client)
    temp = sc.get_messages()
    temp.sort()
    main_message_list.sort()
    assert temp == main_message_list


def test_get_messages_with_old_time():
    clean_up()
    sc = ServerConnector(url, client)
    before = datetime.now(tz=pytz.timezone("America/Denver")).replace(
        hour=22, minute=0, second=0, microsecond=0)

    # this makes it so that we see everthing from two nights ago on
    time_before = before

    temp = sc.get_messages(time_before=time_before)
    temp.sort()
    main_message_list.sort()
    assert temp == []
    clean_up(True)


def test_get_messages_with_time():
    clean_up()
    sc = ServerConnector(url, client)
    temp = []
    sleep(1)
    before = datetime.now(tz=pytz.timezone("America/Denver"))

    # this makes it so that we see everthing from two nights ago on
    time_before = before - timedelta(days=2)

    temp = sc.get_messages(time_before=time_before)
    temp.sort()
    main_message_list.sort()
    assert temp == main_message_list
