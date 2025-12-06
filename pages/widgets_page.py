from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger
import time

logger = Logger.get_logger(__name__)


class WidgetsPage(BasePage):
    """Page object for DemoQA Widgets module."""

    # Date Picker locators
    DATE_PICKER_INPUT = (By.ID, "datePickerMonthYearInput")
    DATE_PICKER_MONTH_YEAR = (By.CLASS_NAME, "react-datepicker__current-month-button")
    DATE_PICKER_DAY = (By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--001']")

    # Slider locators
    SLIDER_INPUT = (By.XPATH, "//input[@type='range']")
    SLIDER_VALUE = (By.ID, "sliderValue")

    # Accordion locators
    ACCORDION_ITEM_1 = (By.ID, "headingOne")
    ACCORDION_CONTENT_1 = (By.ID, "collapseOne")
    ACCORDION_ITEM_2 = (By.ID, "headingTwo")
    ACCORDION_CONTENT_2 = (By.ID, "collapseTwo")
    ACCORDION_ITEM_3 = (By.ID, "headingThree")
    ACCORDION_CONTENT_3 = (By.ID, "collapseThree")

    # Tab locators
    TAB_1 = (By.ID, "tab-tab-1")
    TAB_2 = (By.ID, "tab-tab-2")
    TAB_3 = (By.ID, "tab-tab-3")
    TAB_CONTENT = (By.CLASS_NAME, "nav-content")

    # Tooltip locators
    TOOLTIP_BUTTON = (By.ID, "toolTipButton")
    TOOLTIP_TEXT = (By.CLASS_NAME, "tooltip-inner")

    # Progress Bar locators
    PROGRESS_START_BUTTON = (By.ID, "startStopButton")
    PROGRESS_BAR = (By.CLASS_NAME, "progress-bar")

    def __init__(self, driver, base_url: str):
        """Initialize WidgetsPage."""
        super().__init__(driver, base_url)

    def open_widgets(self):
        """Open the widgets page."""
        self.open("/widgets")
        logger.info("Opened Widgets page")

    # Date Picker methods
    def select_date_from_picker(self, date_string: str):
        """
        Select a date from the date picker.

        Args:
            date_string: Date string in format MM/DD/YYYY
        """
        self.click(self.DATE_PICKER_INPUT)
        self.type_text(self.DATE_PICKER_INPUT, date_string)
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element(*self.DATE_PICKER_INPUT).send_keys(Keys.ENTER)
        logger.info(f"Selected date: {date_string}")

    def get_selected_date(self) -> str:
        """Get the currently selected date from the date picker."""
        date = self.get_attribute(self.DATE_PICKER_INPUT, "value")
        logger.info(f"Retrieved selected date: {date}")
        return date

    # Slider methods
    def set_slider_value(self, value: int):
        """
        Set slider value.

        Args:
            value: Value to set (0-100)
        """
        slider = self.find(self.SLIDER_INPUT)
        if slider:
            self.driver.execute_script(
                f"arguments[0].value = {value};",
                slider
            )
            self.driver.execute_script(
                "arguments[0].dispatchEvent(new Event('input', {{ bubbles: true }}));",
                slider
            )
            logger.info(f"Set slider value to: {value}")
        else:
            logger.warning("Could not find slider element")

    def get_slider_value(self) -> str:
        """Get the current slider value."""
        value = self.get_text(self.SLIDER_VALUE)
        logger.info(f"Retrieved slider value: {value}")
        return value

    # Accordion methods
    def expand_accordion_item(self, item_number: int):
        """
        Expand an accordion item.

        Args:
            item_number: Accordion item number (1, 2, or 3)
        """
        if item_number == 1:
            self.click(self.ACCORDION_ITEM_1)
            logger.info("Expanded accordion item 1")
        elif item_number == 2:
            self.click(self.ACCORDION_ITEM_2)
            logger.info("Expanded accordion item 2")
        elif item_number == 3:
            self.click(self.ACCORDION_ITEM_3)
            logger.info("Expanded accordion item 3")

    def get_accordion_content(self, item_number: int) -> str:
        """
        Get the content of an accordion item.

        Args:
            item_number: Accordion item number (1, 2, or 3)

        Returns:
            Content text of the accordion item
        """
        if item_number == 1:
            content = self.get_text(self.ACCORDION_CONTENT_1)
        elif item_number == 2:
            content = self.get_text(self.ACCORDION_CONTENT_2)
        elif item_number == 3:
            content = self.get_text(self.ACCORDION_CONTENT_3)
        else:
            content = ""

        logger.info(f"Retrieved accordion item {item_number} content")
        return content

    def is_accordion_expanded(self, item_number: int) -> bool:
        """
        Check if an accordion item is expanded.

        Args:
            item_number: Accordion item number (1, 2, or 3)

        Returns:
            Boolean indicating if accordion is expanded
        """
        if item_number == 1:
            locator = self.ACCORDION_CONTENT_1
        elif item_number == 2:
            locator = self.ACCORDION_CONTENT_2
        elif item_number == 3:
            locator = self.ACCORDION_CONTENT_3
        else:
            return False

        is_displayed = self.is_displayed(locator, timeout=5)
        logger.info(f"Accordion item {item_number} expanded: {is_displayed}")
        return is_displayed

    # Tab methods
    def click_tab(self, tab_number: int):
        """
        Click a tab.

        Args:
            tab_number: Tab number (1, 2, or 3)
        """
        if tab_number == 1:
            self.click(self.TAB_1)
            logger.info("Clicked tab 1")
        elif tab_number == 2:
            self.click(self.TAB_2)
            logger.info("Clicked tab 2")
        elif tab_number == 3:
            self.click(self.TAB_3)
            logger.info("Clicked tab 3")

    def get_tab_content(self) -> str:
        """Get the current tab content."""
        content = self.get_text(self.TAB_CONTENT)
        logger.info(f"Retrieved tab content")
        return content

    # Tooltip methods
    def hover_over_tooltip_button(self):
        """Hover over the tooltip button to reveal tooltip."""
        self.hover(self.TOOLTIP_BUTTON)
        logger.info("Hovered over tooltip button")

    def get_tooltip_text(self) -> str:
        """
        Get the tooltip text.

        Returns:
            Tooltip text
        """
        time.sleep(1)  # Wait for tooltip to appear
        tooltip_text = self.get_text(self.TOOLTIP_TEXT)
        logger.info(f"Retrieved tooltip text: {tooltip_text}")
        return tooltip_text

    # Progress Bar methods
    def click_progress_start_button(self):
        """Click the progress bar start/stop button."""
        self.click(self.PROGRESS_START_BUTTON)
        logger.info("Clicked progress bar start button")

    def get_progress_bar_value(self) -> str:
        """
        Get the progress bar value.

        Returns:
            Progress bar value as percentage string
        """
        value = self.get_attribute(self.PROGRESS_BAR, "aria-valuenow")
        logger.info(f"Retrieved progress bar value: {value}")
        return value
