import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utils.logger import Logger

logger = Logger.get_logger(__name__)


class DriverFactory:
    """Factory class to create and manage WebDriver instances."""

    @staticmethod
    def get_driver(browser: str = "chrome", headless: bool = False):
        """
        Get a WebDriver instance based on browser type.

        Args:
            browser: Browser type ('chrome' or 'firefox')
            headless: Run in headless mode (default: False)

        Returns:
            WebDriver instance
        """
        logger.info(f"Creating {browser} WebDriver instance (headless={headless})")

        if browser.lower() == "chrome":
            return DriverFactory._create_chrome_driver(headless)
        elif browser.lower() == "firefox":
            return DriverFactory._create_firefox_driver(headless)
        else:
            logger.error(f"Unsupported browser: {browser}")
            raise ValueError(f"Unsupported browser: {browser}")

    @staticmethod
    def _create_chrome_driver(headless: bool = False):
        """Create a Chrome WebDriver instance."""
        options = webdriver.ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")

        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        logger.info("Chrome WebDriver created successfully")
        return driver

    @staticmethod
    def _create_firefox_driver(headless: bool = False):
        """Create a Firefox WebDriver instance."""
        options = webdriver.FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        options.add_argument("--no-sandbox")

        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        driver.maximize_window()

        logger.info("Firefox WebDriver created successfully")
        return driver

    @staticmethod
    def quit_driver(driver):
        """Quit the WebDriver instance."""
        if driver:
            driver.quit()
            logger.info("WebDriver quit successfully")
