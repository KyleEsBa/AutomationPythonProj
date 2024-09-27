from selenium import webdriver
import pytest
from utilities.readProperties import ReadConfig
@pytest.fixture()
def setup():
    browser=ReadConfig.getIniValueOf("browser")
    if  browser=="Chrome":
        driver=webdriver.Chrome()
    elif browser=="Firefox":
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver