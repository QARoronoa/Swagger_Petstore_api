import configparser


def config():
    param = configparser.ConfigParser()
    param.read('utilities/proprietes.ini')
    return param