# This is the experimental testing suite for this app
#  Tests used to be done via terminal now add tests here


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

    def test_normal_run(self):
        """
            test a normal run
        """
        NAME = "UnitTests.py"
        LOCATION = re.sub(NAME, "", sys.argv[0])

        # loads config file (config)
        try:
            with open(LOCATION + 'config.json', 'r') as f:
                config = json.load(f)
        except IOError:
            print("error missing config file")
            exit(-1)

        print('Entering Debug mode')
        debug = True

        # print('using local server')
        # config['URL']='http://127.0.0.1:5000'

        print('uploading test data')
        messageList = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
        for i in messageList:
            postProcess = MyThread(self.postMessage, postData={
                                   'message': i, '_to': self.test})
            postProcess.start()

        self.assertEqual(main(config['SLEEP'], self.url, self.delUrl, debug,
                              config['EXPIRATION'], config['MORNING'], config['EVENING']), 1)

    def test_sleep_exit(self):
        # python code/main.py -d -t
        pass

    def test_sleep(self):
        pass
        # elif(i == "-t"):  # makes server local
        #     print('testing sleep')
        #     testSleep = True


if __name__ == '__main__':
    unittest.main()
