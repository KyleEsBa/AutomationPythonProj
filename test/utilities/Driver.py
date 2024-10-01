from selenium import webdriver

from test.utilities.readProperties import ReadConfig


class Driver:
    _instance = None
    _driver = None

    @classmethod
    def get_instance(cls):
        """Ensure only one instance of the WebDriver is created."""
        browser=ReadConfig.getIniValueOf("browser")
        if cls._instance is None:
            cls._instance = cls()
            if browser.lower() == 'chrome':
                cls._driver = webdriver.Chrome()
            elif browser.lower() == 'firefox':
                cls._driver = webdriver.Firefox()
            else:
                raise ValueError(f"Unsupported browser: {browser}")
        return cls._instance

    @staticmethod
    def get_driver():
        """Return the WebDriver instance."""
        return Driver._driver

    @staticmethod
    def quit():
        """Quit the WebDriver instance."""
        if Driver._driver:
            Driver._driver.quit()
            Driver._instance = None  # Reset instance to allow recreation if needed
            Driver._driver = None
