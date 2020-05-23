import uiautomator2 as u2


def connect():
    d = u2.connect_usb('UYT0217B17005916')
    return d
