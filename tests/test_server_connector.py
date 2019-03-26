# Author Matt Bussing
from datetime import datetime, timedelta
from time import sleep

import pytz
import requests

from distancepi.server_connector import ServerConnector

url = "https://distance-pi.herokuapp.com/"
client = "test"
client_url = url + client
del_url = client_url
post_url = url + "/"

thinking_of = "thinking-of"
thinking_url = client_url + "/" + thinking_of

main_message_list = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
main_message_list.sort()

messages_deleted = False


def clean_up(need_to: bool = False):
    global messages_deleted
    if not messages_deleted or need_to:
        messages_deleted = True
        _delete_all_messages()
        for i in main_message_list:
            _post_message(post_data={'message': i, '_to': client})


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
    temp = sc.get_data()[0]
    temp.sort()
    assert temp == main_message_list


def test_get_messages_with_old_time():
    clean_up()
    sc = ServerConnector(url, client)
    before = datetime.now(tz=pytz.timezone("America/Denver")).replace(
        hour=22, minute=0, second=0, microsecond=0)

    # this makes it so that we see everthing from two nights ago on
    time_before = before
    temp = sc.get_data(time_before=time_before)[0]
    temp.sort()
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

    temp = sc.get_data(time_before=time_before)[0]
    temp.sort()
    assert temp == main_message_list


def _get_all_messages_and_count():
    req_data = requests.get(url=client_url)
    message_list = []
    count = 0
    if(req_data.status_code == 200):
        data = req_data.json()
        message_list = data['messages']
        if data['count'] is not None:
            count = data['count']
    else:
        print(req_data.status_code)
    return (message_list, count)


def _increaset_count(increment):
    return requests.post(url=thinking_url, json={
        "increase_by": increment})


def test_count_built_in():
    assert 200 == requests.delete(url=thinking_url).status_code
    increment = 2
    _increaset_count(increment)
    temp = _get_all_messages_and_count()[1]
    assert increment == temp
    old = increment
    increment = 5
    _increaset_count(increment)
    temp = _get_all_messages_and_count()[1]
    assert old + increment == temp


def test_count():
    sc = ServerConnector(url, client)
    assert 200 == requests.delete(url=thinking_url).status_code
    increment = 2
    _increaset_count(increment)
    temp = sc.get_data()[1]
    assert increment == temp
    old = increment
    increment = 5
    _increaset_count(increment)
    temp = sc.get_data()[1]
    assert old + increment == temp


def test_increase_count_pt_2():
    # this is just to make sure that everything
    # works by deleting and trying again
    test_count_built_in()
    test_count()
