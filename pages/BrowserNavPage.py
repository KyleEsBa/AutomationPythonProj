from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class BrowserNavPage:
    tbx_search_name="q"
    lnk_option_xpath="//h3[text()='Downloads | ChromeDriver - Chrome for Developers']"

    def __init__(self, driver):
        self.driver=driver

    def searchWord(self, word):
        tbx_search=self.driver.find_element('name',self.tbx_search_name)
        tbx_search.clear()
        tbx_search.send_keys(word)
        tbx_search.send_keys(Keys.ENTER)

    def getElementDisplayed(self):
        try:
            lnk_option=self.driver.find_element('xpath', self.lnk_option_xpath)
            return lnk_option.is_displayed()
        except NoSuchElementException:
            return False