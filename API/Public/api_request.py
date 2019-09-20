import requests
import json


def get(url, headers=None, timeout=None):
    re = requests.get(url=url, headers=headers, timeout=timeout)
    # response = re.text
    # response = json.loads(response)
    # print(response['reward_description'])
    if re.status_code != 200:
        print(re.status_code)
    return re.status_code


def post(url,  data, headers=None, timeout=None):
    re = requests.post(url=url, data=data, headers=headers, timeout=timeout)
    if re.status_code != 200:
        print(re.status_code)
    return re.status_code, re.text
    # json.loads()是将字符串转化成字典
    # json.dumps()是将字典转化成字符串


