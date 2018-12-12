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

    # elif(i == "-u"):  # This sets up test data
    #      print('uploading test data')
    #      d.messageList = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
    #
    #      def postMessage(postData, url, verbose=False):
    #          r = requests.post(url=url, json=postData)
    #          print(r)
    #          return r
    #
    #      for i in messageList:
    #          postProcess = MyThread(postMessage, postData={
    #                                 'message': i, '_to': 'Matt'})
    #          postProcess.start()
    #
    #  elif(i == "-e"):  # This sets up test data
    #      print('setting small expiration date for database entries')
    #      d.config['EXPIRATION'] = 5 * 60

    def deleteMessage(self):
        return requests.delete(url=self.delUrl, json=self.delJson)

    def postMessage(self, postData):
        return requests.post(url=self.postUrl, json=postData)

    def test_normal_run(self):
        """
            test a normal run
        """
        d = Device(name="UnitTests.py", tests=True)
        m = d.main()
        print('uploading test data')
        messageList = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
        for i in messageList:
            postProcess = MyThread(self.postMessage, postData={
                                   'message': i, '_to': self.test})
            postProcess.start()

        self.assertEqual(d.main().sort(), messageList.sort())

        # def test_sleep_exit(self):
        #     # python code/main.py -d -t
        #     pass
        #
        # def test_sleep(self):
        #     pass
        # elif(i == "-t"):  # makes server local
        #     print('testing sleep')
        #     testSleep = True


if __name__ == '__main__':
    unittest.main()
