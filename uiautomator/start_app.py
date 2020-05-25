from connect_devices import connect
'''
用户app_crash时启动app回到首页
'''


def start():
    d = connect()
    d.app_start('com.xiaoniu.showlive')


start()
