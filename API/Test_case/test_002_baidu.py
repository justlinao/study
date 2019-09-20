import unittest
from Public.api_request import get
from Public.log import get_log
import requests
url = 'https://www.baidu.com/'
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


class Test_baidu(unittest.TestCase):
    def setUp(self):
        pass

    def test_baidu(self):
        self.get = get(url, header, timeout=0.5)
        self.assertEqual(self.get, 200, self.get)
        get_log().info('百度_请求成功')

    def tearDown(self):
        pass


if __name__ == '__main__':
    Test_baidu().test_baidu()
