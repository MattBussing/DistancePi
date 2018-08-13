import unittest

import requests

import main

class TestAdd(unittest.TestCase):
    postUrl ='http://127.0.0.1:5000/'
    delUrl ='http://127.0.0.1:5000/Matt'

    delJson = {'message':'value'}

    def deleteMessage(self):
        return requests.delete(url=self.delUrl, json=self.delJson)

    def postMessage(self, postData):
        return requests.post(url=self.postUrl, json=postData)

    def test(self):
        """
            Checks to see if it deletes the message
        """
        messageList = [ 'lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']
        for i in messageList:
            self.postMessage( {'message':i, '_to':'Matt'})

        self.assertEqual(main.main(list('-d'), test=True), 'success')


if __name__ == '__main__':
    unittest.main()
