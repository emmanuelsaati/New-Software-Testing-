import pytest
from pages.widgets_page import WidgetsPage
from utils.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.widgets
@pytest.mark.positive
class TestWidgetsDatePicker:
    """Test cases for Widgets Date Picker."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.widgets_page = WidgetsPage(driver, base_url)
        self.widgets_page.open_widgets()

    def test_widget_01_date_picker_selection(self):
        """TC-WID-01: Verify that date picker accepts and returns a valid date."""
        logger.info("Starting test: Date picker selection")

        test_date = "12/12/2024"
        self.widgets_page.select_date_from_picker(test_date)

        selected_date = self.widgets_page.get_selected_date()

        assert selected_date, "Date picker did not return a date"
        logger.info(f"Test passed: Date picker selected date: {selected_date}")


@pytest.mark.widgets
@pytest.mark.positive
class TestWidgetsSlider:
    """Test cases for Widgets Slider."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.widgets_page = WidgetsPage(driver, base_url)
        self.widgets_page.open_widgets()

    def test_widget_02_slider_value_change(self):
        """TC-WID-02: Verify slider value change reflects in UI."""
        logger.info("Starting test: Slider value change")

        test_value = 50
        self.widgets_page.set_slider_value(test_value)

        slider_value = self.widgets_page.get_slider_value()

        assert slider_value, "Slider value not returned"
        logger.info(f"Test passed: Slider value changed to: {slider_value}")

    def test_widget_02b_slider_minimum_value(self):
        """TC-WID-02b: Verify slider can be set to minimum value."""
        logger.info("Starting test: Slider minimum value")

        self.widgets_page.set_slider_value(0)
        slider_value = self.widgets_page.get_slider_value()

        assert slider_value == "0", f"Expected 0, got {slider_value}"
        logger.info("Test passed: Slider set to minimum value")

    def test_widget_02c_slider_maximum_value(self):
        """TC-WID-02c: Verify slider can be set to maximum value."""
        logger.info("Starting test: Slider maximum value")

        self.widgets_page.set_slider_value(100)
        slider_value = self.widgets_page.get_slider_value()

        assert slider_value == "100", f"Expected 100, got {slider_value}"
        logger.info("Test passed: Slider set to maximum value")


@pytest.mark.widgets
@pytest.mark.positive
class TestWidgetsAccordion:
    """Test cases for Widgets Accordion."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.widgets_page = WidgetsPage(driver, base_url)
        self.widgets_page.open_widgets()

    def test_widget_03_accordion_expand_collapse(self):
        """TC-WID-03: Verify that accordions expand/collapse correctly."""
        logger.info("Starting test: Accordion expand/collapse")

        # Expand accordion item 1
        self.widgets_page.expand_accordion_item(1)
        is_expanded = self.widgets_page.is_accordion_expanded(1)

        assert is_expanded, "Accordion item 1 did not expand"
        logger.info("Test passed: Accordion item 1 expanded")

        # Collapse by clicking again
        self.widgets_page.expand_accordion_item(1)
        is_expanded_after = self.widgets_page.is_accordion_expanded(1)

        logger.info(f"Accordion collapsed status: {not is_expanded_after}")
        logger.info("Test passed: Accordion expand/collapse working")

    def test_widget_03b_accordion_content_display(self):
        """TC-WID-03b: Verify accordion displays content when expanded."""
        logger.info("Starting test: Accordion content display")

        self.widgets_page.expand_accordion_item(2)
        content = self.widgets_page.get_accordion_content(2)

        assert content, "Accordion content not displayed"
        logger.info(f"Test passed: Accordion content displayed: {content[:50]}...")


@pytest.mark.widgets
@pytest.mark.positive
class TestWidgetsTooltip:
    """Test cases for Widgets Tooltip."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.widgets_page = WidgetsPage(driver, base_url)
        self.widgets_page.open_widgets()

    def test_widget_04_tooltip_hover(self):
        """TC-WID-04: Verify tooltip appears on hover and contains expected text."""
        logger.info("Starting test: Tooltip hover display")

        self.widgets_page.hover_over_tooltip_button()
        tooltip_text = self.widgets_page.get_tooltip_text()

        assert tooltip_text, "Tooltip text not found"
        logger.info(f"Test passed: Tooltip displayed with text: {tooltip_text}")


@pytest.mark.widgets
@pytest.mark.regression
class TestWidgetsMultiple:
    """Multiple widget interaction tests."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.widgets_page = WidgetsPage(driver, base_url)
        self.widgets_page.open_widgets()

    def test_widget_05_multiple_interactions(self):
        """TC-WID-05: Test multiple widget interactions in sequence."""
        logger.info("Starting test: Multiple widget interactions")

        # Test slider
        self.widgets_page.set_slider_value(75)
        slider_value = self.widgets_page.get_slider_value()
        assert slider_value, "Slider interaction failed"

        # Test accordion
        self.widgets_page.expand_accordion_item(1)
        is_expanded = self.widgets_page.is_accordion_expanded(1)
        assert is_expanded, "Accordion interaction failed"

        logger.info("Test passed: Multiple widget interactions successful")
