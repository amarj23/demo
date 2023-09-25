import configparser

config = configparser.RawConfigParser()

config.read('C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Configuration\\config.ini')


class Readvalues:

    @staticmethod
    def getusername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('login info', 'password')
        return password

    @staticmethod
    def first_name():
        firstname = config.get('login info', 'first_name')
        return firstname

    @staticmethod
    def last_name():
        lastname = config.get('login info', 'last_name')
        return lastname

    @staticmethod
    def zip_code():
        zipcode = config.get('login info', 'zip_code')
        return zipcode

    @staticmethod
    def url():
        url = config.get('login info', 'url')
        return url
