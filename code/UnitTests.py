# This is the experimental testing suite for this app

import json
import re
import sys
import unittest

import requests

from main import Device
from my_threads import MyThread


class TestAdd(unittest.TestCase):
    url = 'https://distance-pi.herokuapp.com'
    postUrl = url + '/'
    test = 'Matt'
    delUrl = url + '/' + test

    delJson = {'message': 'value'}
    postJson = {'message': 'value', '_to': 'testing'}

    def deleteMessage(self):
        return requests.delete(url=self.delUrl, json=self.delJson)

    def postMessage(self, postData):
        return requests.post(url=self.postUrl, json=postData)

    def device(self, d):
        m = d.main()
        print('uploading test data')
        self.messageList = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
        for i in self.messageList:
            postProcess = MyThread(self.postMessage, postData={
                                   'message': i, '_to': self.test})
            postProcess.start()

    def test_normal_run(self):
        print("\n############normal_run")
        # test a normal run
        d = Device(name="UnitTests.py", tests=True,
                   onComputer=True)
        self.device(d)
        self.assertEqual(d.main().sort(), self.messageList.sort())

    def test_rpi(self):
        print("rpi")
        d = Device(name="UnitTests.py", tests=True, onComputer=False)
        self.device(d)
        self.assertEqual(d.main().sort(), self.messageList.sort())

    def test_sleep_variable(self):
        print("\n##############sleep_variable")
        d = Device(name="UnitTests.py", tests=True,
                   sleepOn=True, onComputer=True, verbose=True)
        self.device(d)
        print(self.messageList)
        self.assertEqual(d.main().sort(), self.messageList.sort())


if __name__ == '__main__':
    unittest.main()
