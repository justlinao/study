from connect_devices import connect
d = connect()


def call():
    d(text='电话').click()
    d(text='1').click()
    d(text='8').click()
    d(text='1').click()
    d(text='1').click()
    d(text='9').click()
    d(text='6').click()
    d(text='7').click()


if __name__ == '__main__':
    call()
