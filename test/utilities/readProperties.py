import configparser

config=configparser.RawConfigParser()
config.read("../../configuration.ini")

class ReadConfig:
    @staticmethod
    def getIniValueOf(key):
        value=config.get('common info',key)
        return value