import time

import pytest

from pages.BrowserNavPage import BrowserNavPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities.ExcelUtils import ExcelUtils
from utilities.Driver import Driver
@pytest.mark.regression
class Test_Browser:
    baseURL=ReadConfig.getIniValueOf("baseURL")
    logger=LogGen.loggen()
    @pytest.mark.wip
    def test_Sample(self, driver):
        self.logger.info("***Test_Browser***")
        self.logger.info("Verify search option is displayed")
        driver.get(self.baseURL)
        #time.sleep(2)
        self.browserNavPage=BrowserNavPage(driver)
        for i in range (2, ExcelUtils.getRowCount()+1):
            self.browserNavPage.searchWord(ExcelUtils.readData(i,1))
        if self.browserNavPage.getElementDisplayed():
            self.logger.info("Option is displayed")
            assert True
        else:
            self.logger.error("Option is not displayed")
            driver.save_screenshot("C:\\Users\\User\\IdeaProjects\\AutomationPythonProj\\screenshots\\"+"test_Sample.png")
            assert False