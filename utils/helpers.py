import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import Logger

logger = Logger.get_logger(__name__)


class WaitHelper:
    """Helper class for wait operations."""

    @staticmethod
    def wait_for_element_visible(driver, locator: tuple, timeout: int = 10):
        """
        Wait for an element to be visible.

        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            WebElement if visible, None otherwise
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            logger.debug(f"Element {locator} is visible")
            return element
        except TimeoutException:
            logger.warning(f"Timeout waiting for element {locator} to be visible")
            return None

    @staticmethod
    def wait_for_element_clickable(driver, locator: tuple, timeout: int = 10):
        """
        Wait for an element to be clickable.

        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            WebElement if clickable, None otherwise
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            logger.debug(f"Element {locator} is clickable")
            return element
        except TimeoutException:
            logger.warning(f"Timeout waiting for element {locator} to be clickable")
            return None

    @staticmethod
    def wait_for_element_presence(driver, locator: tuple, timeout: int = 10):
        """
        Wait for an element to be present in DOM.

        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            WebElement if present, None otherwise
        """
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logger.debug(f"Element {locator} is present in DOM")
            return element
        except TimeoutException:
            logger.warning(f"Timeout waiting for element {locator} to be present")
            return None

    @staticmethod
    def wait_for_text_in_element(driver, locator: tuple, text: str, timeout: int = 10):
        """
        Wait for specific text to appear in an element.

        Args:
            driver: WebDriver instance
            locator: Tuple of (By, value)
            text: Text to wait for
            timeout: Timeout in seconds

        Returns:
            Boolean indicating success
        """
        try:
            WebDriverWait(driver, timeout).until(
                EC.text_to_be_present_in_element(locator, text)
            )
            logger.debug(f"Text '{text}' found in element {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Timeout waiting for text '{text}' in element {locator}")
            return False

    @staticmethod
    def wait_for_url_to_change(driver, original_url: str, timeout: int = 10):
        """
        Wait for URL to change from original.

        Args:
            driver: WebDriver instance
            original_url: Original URL to compare
            timeout: Timeout in seconds

        Returns:
            Boolean indicating success
        """
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.current_url != original_url
            )
            logger.debug(f"URL changed from {original_url}")
            return True
        except TimeoutException:
            logger.warning(f"Timeout waiting for URL to change from {original_url}")
            return False


class RetryHelper:
    """Helper class for retry operations."""

    @staticmethod
    def retry_operation(func, max_attempts: int = 3, delay: float = 1.0, *args, **kwargs):
        """
        Retry an operation multiple times.

        Args:
            func: Function to retry
            max_attempts: Maximum number of attempts
            delay: Delay between attempts in seconds
            *args: Positional arguments for function
            **kwargs: Keyword arguments for function

        Returns:
            Function result or None
        """
        for attempt in range(1, max_attempts + 1):
            try:
                logger.debug(f"Attempt {attempt}/{max_attempts} for operation {func.__name__}")
                result = func(*args, **kwargs)
                logger.debug(f"Operation {func.__name__} succeeded on attempt {attempt}")
                return result
            except Exception as e:
                logger.warning(f"Attempt {attempt} failed: {str(e)}")
                if attempt < max_attempts:
                    time.sleep(delay)
                else:
                    logger.error(f"Operation {func.__name__} failed after {max_attempts} attempts")
                    raise

        return None
