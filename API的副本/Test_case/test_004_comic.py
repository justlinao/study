import unittest
from Public.api_request import post
from Public.log import get_log
import requests
url = 'http://mp-boe.toutiao.com/esign/api/callback/syncCertifyStatus'
data = {'apply_id': '1', 'certify_state': 'pald', 'remark': '123'}
headers = {'Content-type': 'application/x-www-form-urlencoded'}


class Comic(unittest.TestCase):
    def setUp(self):
        pass

    def test_comic(self):
        self.post = post(url=url, data=data, headers=headers)
        self.assertEqual(self.post, (200, 'success'))
        print(self.post)

    def tearDown(self):
        pass


if __name__ == '__main__':
    Comic().test_comic()
