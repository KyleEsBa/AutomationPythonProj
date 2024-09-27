import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\User\\IdeaProjects\\AutomationPythonProj\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def getIniValueOf(key):
        value=config.get('common info',key)
        return value