import unittest
from Public.api_request import get
from Public.log import get_log
import requests
url = 'https://www.jianshu.com/notes/39145310/rewards?count=20'
header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}


class Test_jianshu(unittest.TestCase):
    def setUp(self):
        pass

    def test_jianshu(self):
        self.get = get(url, header)
        self.assertEqual(self.get, 200, self.get)
        get_log().info('简书请求的结果%s' % self.get)

    def tearDown(self):
        pass


if __name__ == '__main__':
    Test_jianshu().test_jianshu()
