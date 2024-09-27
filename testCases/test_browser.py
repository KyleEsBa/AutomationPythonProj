import time
from pages.BrowserNavPage import BrowserNavPage
from utilities.readProperties import ReadConfig
class Test_Browser:
    baseURL=ReadConfig.getIniValueOf("baseURL")
    word=ReadConfig.getIniValueOf("word")
    def test_Sample(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        #time.sleep(2)
        self.browserNavPage=BrowserNavPage(self.driver)
        self.browserNavPage.searchWord(self.word)
        print(self.browserNavPage.getElementDisplayed())
        if self.browserNavPage.getElementDisplayed():
            print("Option is displayed")
            assert True
        else:
            print("Option is not displayed")
            self.driver.save_screenshot("C:\\Users\\User\\IdeaProjects\\AutomationPythonProj\\screenshots\\"+"test_Sample.png")
            assert False
        self.driver.close()