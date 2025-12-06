from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from utils.logger import Logger
from utils.helpers import WaitHelper
import os
from datetime import datetime

logger = Logger.get_logger(__name__)


class BasePage:
    """Base page class providing common methods for page objects."""

    def __init__(self, driver, base_url: str):
        """
        Initialize BasePage.

        Args:
            driver: WebDriver instance
            base_url: Base URL for the application
        """
        self.driver = driver
        self.base_url = base_url
        self.wait_helper = WaitHelper()
        self.screenshot_dir = "tests_output/screenshots"
        os.makedirs(self.screenshot_dir, exist_ok=True)

    def open(self, url: str = None):
        """
        Open a URL.

        Args:
            url: URL to open (relative to base_url if not full URL)
        """
        if url is None:
            url = self.base_url
        elif not url.startswith("http"):
            url = self.base_url + url

        logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def find(self, locator: tuple):
        """
        Find an element by locator.

        Args:
            locator: Tuple of (By, value)

        Returns:
            WebElement or None
        """
        try:
            element = self.driver.find_element(*locator)
            logger.debug(f"Element found: {locator}")
            return element
        except NoSuchElementException:
            logger.warning(f"Element not found: {locator}")
            return None

    def find_elements(self, locator: tuple):
        """
        Find multiple elements by locator.

        Args:
            locator: Tuple of (By, value)

        Returns:
            List of WebElements
        """
        try:
            elements = self.driver.find_elements(*locator)
            logger.debug(f"Found {len(elements)} elements: {locator}")
            return elements
        except NoSuchElementException:
            logger.warning(f"No elements found: {locator}")
            return []

    def click(self, locator: tuple, timeout: int = 10):
        """
        Click an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_clickable(self.driver, locator, timeout)
            if element:
                element.click()
                logger.info(f"Clicked element: {locator}")
            else:
                logger.error(f"Could not click element (not clickable): {locator}")
        except Exception as e:
            logger.error(f"Failed to click element {locator}: {str(e)}")
            raise

    def type_text(self, locator: tuple, text: str, timeout: int = 10):
        """
        Type text into an element.

        Args:
            locator: Tuple of (By, value)
            text: Text to type
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                element.clear()
                element.send_keys(text)
                logger.info(f"Typed text '{text}' into element: {locator}")
            else:
                logger.error(f"Could not type into element (not visible): {locator}")
        except Exception as e:
            logger.error(f"Failed to type into element {locator}: {str(e)}")
            raise

    def get_text(self, locator: tuple, timeout: int = 10) -> str:
        """
        Get text from an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            Text content of element
        """
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                text = element.text
                logger.debug(f"Retrieved text '{text}' from element: {locator}")
                return text
            else:
                logger.warning(f"Could not get text from element (not visible): {locator}")
                return ""
        except Exception as e:
            logger.error(f"Failed to get text from element {locator}: {str(e)}")
            return ""

    def is_displayed(self, locator: tuple, timeout: int = 10) -> bool:
        """
        Check if an element is displayed.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            Boolean indicating if element is displayed
        """
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            is_visible = element is not None and element.is_displayed()
            logger.debug(f"Element {locator} is_displayed: {is_visible}")
            return is_visible
        except Exception as e:
            logger.debug(f"Element {locator} not displayed: {str(e)}")
            return False

    def is_enabled(self, locator: tuple) -> bool:
        """
        Check if an element is enabled.

        Args:
            locator: Tuple of (By, value)

        Returns:
            Boolean indicating if element is enabled
        """
        try:
            element = self.find(locator)
            if element:
                is_en = element.is_enabled()
                logger.debug(f"Element {locator} is_enabled: {is_en}")
                return is_en
            return False
        except Exception as e:
            logger.debug(f"Could not check if element is enabled {locator}: {str(e)}")
            return False

    def get_attribute(self, locator: tuple, attribute: str, timeout: int = 10) -> str:
        """
        Get an attribute value from an element.

        Args:
            locator: Tuple of (By, value)
            attribute: Attribute name
            timeout: Timeout in seconds

        Returns:
            Attribute value
        """
        try:
            element = self.wait_helper.wait_for_element_present(self.driver, locator, timeout)
            if element:
                value = element.get_attribute(attribute)
                logger.debug(f"Retrieved attribute '{attribute}' = '{value}' from element: {locator}")
                return value
            else:
                logger.warning(f"Could not get attribute from element (not present): {locator}")
                return ""
        except Exception as e:
            logger.error(f"Failed to get attribute '{attribute}' from element {locator}: {str(e)}")
            return ""

    def hover(self, locator: tuple, timeout: int = 10):
        """
        Hover over an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                ActionChains(self.driver).move_to_element(element).perform()
                logger.info(f"Hovered over element: {locator}")
            else:
                logger.warning(f"Could not hover over element (not visible): {locator}")
        except Exception as e:
            logger.error(f"Failed to hover over element {locator}: {str(e)}")
            raise

    def double_click(self, locator: tuple, timeout: int = 10):
        """
        Double-click an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_clickable(self.driver, locator, timeout)
            if element:
                ActionChains(self.driver).double_click(element).perform()
                logger.info(f"Double-clicked element: {locator}")
            else:
                logger.warning(f"Could not double-click element (not clickable): {locator}")
        except Exception as e:
            logger.error(f"Failed to double-click element {locator}: {str(e)}")
            raise

    def right_click(self, locator: tuple, timeout: int = 10):
        """
        Right-click an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                ActionChains(self.driver).context_click(element).perform()
                logger.info(f"Right-clicked element: {locator}")
            else:
                logger.warning(f"Could not right-click element (not visible): {locator}")
        except Exception as e:
            logger.error(f"Failed to right-click element {locator}: {str(e)}")
            raise

    def drag_and_drop(self, source_locator: tuple, target_locator: tuple, timeout: int = 10):
        """
        Drag an element to another element.

        Args:
            source_locator: Tuple of (By, value) for source element
            target_locator: Tuple of (By, value) for target element
            timeout: Timeout in seconds
        """
        try:
            source = self.wait_helper.wait_for_element_visible(self.driver, source_locator, timeout)
            target = self.wait_helper.wait_for_element_visible(self.driver, target_locator, timeout)

            if source and target:
                ActionChains(self.driver).drag_and_drop(source, target).perform()
                logger.info(f"Dragged element {source_locator} to {target_locator}")
            else:
                logger.warning(f"Could not drag and drop (elements not visible)")
        except Exception as e:
            logger.error(f"Failed to drag and drop: {str(e)}")
            raise

    def select_dropdown_by_value(self, locator: tuple, value: str, timeout: int = 10):
        """
        Select an option from a dropdown by value.

        Args:
            locator: Tuple of (By, value) for select element
            value: Value to select
            timeout: Timeout in seconds
        """
        try:
            from selenium.webdriver.support.select import Select

            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                select = Select(element)
                select.select_by_value(value)
                logger.info(f"Selected dropdown value '{value}' from element: {locator}")
            else:
                logger.warning(f"Could not select dropdown (not visible): {locator}")
        except Exception as e:
            logger.error(f"Failed to select dropdown option {locator}: {str(e)}")
            raise

    def select_dropdown_by_text(self, locator: tuple, text: str, timeout: int = 10):
        """
        Select an option from a dropdown by visible text.

        Args:
            locator: Tuple of (By, value) for select element
            text: Visible text to select
            timeout: Timeout in seconds
        """
        try:
            from selenium.webdriver.support.select import Select

            element = self.wait_helper.wait_for_element_visible(self.driver, locator, timeout)
            if element:
                select = Select(element)
                select.select_by_visible_text(text)
                logger.info(f"Selected dropdown text '{text}' from element: {locator}")
            else:
                logger.warning(f"Could not select dropdown (not visible): {locator}")
        except Exception as e:
            logger.error(f"Failed to select dropdown by text {locator}: {str(e)}")
            raise

    def submit_form(self, form_locator: tuple, timeout: int = 10):
        """
        Submit a form.

        Args:
            form_locator: Tuple of (By, value) for form element
            timeout: Timeout in seconds
        """
        try:
            form = self.wait_helper.wait_for_element_present(self.driver, form_locator, timeout)
            if form:
                form.submit()
                logger.info(f"Submitted form: {form_locator}")
            else:
                logger.warning(f"Could not submit form (not present): {form_locator}")
        except Exception as e:
            logger.error(f"Failed to submit form {form_locator}: {str(e)}")
            raise

    def screenshot(self, name: str = None) -> str:
        """
        Take a screenshot.

        Args:
            name: Name for the screenshot file

        Returns:
            Path to the screenshot file
        """
        if name is None:
            name = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")[:-3]
        filename = f"{name}_{timestamp}.png"
        filepath = os.path.join(self.screenshot_dir, filename)

        self.driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        return filepath

    def wait_for_url_contains(self, text: str, timeout: int = 10) -> bool:
        """
        Wait for URL to contain specific text.

        Args:
            text: Text to wait for in URL
            timeout: Timeout in seconds

        Returns:
            Boolean indicating success
        """
        try:
            from selenium.webdriver.support import expected_conditions as EC

            WebDriverWait(self.driver, timeout).until(
                EC.url_contains(text)
            )
            logger.info(f"URL contains '{text}'")
            return True
        except TimeoutException:
            logger.warning(f"Timeout waiting for URL to contain '{text}'")
            return False

    def scroll_to_element(self, locator: tuple, timeout: int = 10):
        """
        Scroll to an element.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds
        """
        try:
            element = self.wait_helper.wait_for_element_present(self.driver, locator, timeout)
            if element:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                logger.info(f"Scrolled to element: {locator}")
            else:
                logger.warning(f"Could not scroll to element (not present): {locator}")
        except Exception as e:
            logger.error(f"Failed to scroll to element {locator}: {str(e)}")
            raise

    def switch_to_frame(self, frame_locator: tuple, timeout: int = 10):
        """
        Switch to an iframe.

        Args:
            frame_locator: Tuple of (By, value) for iframe element
            timeout: Timeout in seconds
        """
        try:
            frame = self.wait_helper.wait_for_element_present(self.driver, frame_locator, timeout)
            if frame:
                self.driver.switch_to.frame(frame)
                logger.info(f"Switched to frame: {frame_locator}")
            else:
                logger.warning(f"Could not switch to frame (not present): {frame_locator}")
        except Exception as e:
            logger.error(f"Failed to switch to frame {frame_locator}: {str(e)}")
            raise

    def switch_to_default_content(self):
        """Switch back to main content from iframe."""
        self.driver.switch_to.default_content()
        logger.info("Switched back to default content")

    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = 10) -> bool:
        """
        Wait for an element to disappear.

        Args:
            locator: Tuple of (By, value)
            timeout: Timeout in seconds

        Returns:
            Boolean indicating success
        """
        try:
            from selenium.webdriver.support import expected_conditions as EC

            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(locator)
            )
            logger.info(f"Element disappeared: {locator}")
            return True
        except TimeoutException:
            logger.warning(f"Timeout waiting for element to disappear: {locator}")
            return False
