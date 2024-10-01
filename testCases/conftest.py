import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.Driver import Driver
@pytest.fixture(scope="session")
def driver():
    Driver.get_instance()
    driver = Driver.get_driver()
    yield driver
    Driver.quit()
    '''
def setup():
    if  browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="Firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver'''



def reportsConfigure(config):
    config._metadata['Project name']='Company project'
    config._metadata['Module Name']='Project module'
    config._metadata['Team']='Automation team'