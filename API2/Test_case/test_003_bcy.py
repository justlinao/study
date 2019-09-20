import unittest
from Public.api_request import get
from Public.log import get_log
import requests
url = 'https://bcy.net/'
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


class Test_bcy(unittest.TestCase):
    def setUp(self):
        pass

    def test_bcy(self):
        self.get = get(url, header)
        self.assertEqual(self.get, 200, self.get)
        get_log().info('bcy请求的结果%s' % self.get)

    def tearDown(self):
        pass


if __name__ == '__main__':
    Test_bcy().test_bcy()
