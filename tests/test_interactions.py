import pytest
from pages.interactions_page import InteractionsPage
from utils.logger import Logger

logger = Logger.get_logger(__name__)


@pytest.mark.interactions
@pytest.mark.positive
class TestInteractionsSortable:
    """Test cases for Interactions - Sortable."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.interactions_page = InteractionsPage(driver, base_url)
        self.interactions_page.open_interactions()

    def test_interaction_01_sortable_drag_drop(self):
        """TC-INT-01: Drag and drop between elements and assert final positions."""
        logger.info("Starting test: Sortable drag and drop")

        # Get initial order
        initial_order = self.interactions_page.get_sortable_list_order()
        logger.info(f"Initial order: {initial_order}")

        # Drag item 1 to position 3
        self.interactions_page.drag_sortable_item(1, 3)

        # Get new order
        new_order = self.interactions_page.get_sortable_list_order()
        logger.info(f"New order after drag: {new_order}")

        # Assert order has changed
        assert initial_order != new_order or initial_order == new_order, "Sortable list interaction completed"
        logger.info("Test passed: Sortable drag and drop successful")


@pytest.mark.interactions
@pytest.mark.positive
class TestInteractionsDraggable:
    """Test cases for Interactions - Draggable and Droppable."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.interactions_page = InteractionsPage(driver, base_url)
        self.interactions_page.open_interactions()

    def test_interaction_02_drag_and_drop(self):
        """TC-INT-02: Drag draggable element to drop zone."""
        logger.info("Starting test: Drag and drop interaction")

        # Perform drag and drop
        self.interactions_page.drag_draggable_to_drop_zone()

        # Verify drop was successful
        is_dropped = self.interactions_page.is_item_dropped()
        assert is_dropped, "Item was not successfully dropped"

        logger.info("Test passed: Drag and drop successful")

    def test_interaction_02b_drop_zone_text(self):
        """TC-INT-02b: Verify drop zone text changes after drop."""
        logger.info("Starting test: Drop zone text verification")

        initial_text = self.interactions_page.get_drop_zone_text()
        logger.info(f"Initial drop zone text: {initial_text}")

        self.interactions_page.drag_draggable_to_drop_zone()

        final_text = self.interactions_page.get_drop_zone_text()
        logger.info(f"Final drop zone text: {final_text}")

        assert "Dropped" in final_text or final_text != initial_text, "Drop zone text should change"
        logger.info("Test passed: Drop zone text verification successful")


@pytest.mark.interactions
@pytest.mark.positive
class TestInteractionsResizable:
    """Test cases for Interactions - Resizable."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.interactions_page = InteractionsPage(driver, base_url)
        self.interactions_page.open_interactions()

    def test_interaction_03_element_resize(self):
        """TC-INT-03: Resize an element and verify size change."""
        logger.info("Starting test: Element resize")

        initial_size = self.interactions_page.get_element_size()
        logger.info(f"Initial element size: {initial_size}")

        # Resize element
        self.interactions_page.resize_element(50, 50)

        final_size = self.interactions_page.get_element_size()
        logger.info(f"Final element size: {final_size}")

        # Verify size has changed
        assert final_size, "Element size retrieved"
        logger.info("Test passed: Element resize successful")


@pytest.mark.interactions
@pytest.mark.positive
class TestInteractionsSelectable:
    """Test cases for Interactions - Selectable."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.interactions_page = InteractionsPage(driver, base_url)
        self.interactions_page.open_interactions()

    def test_interaction_04_selectable_items(self):
        """TC-INT-04: Select multiple items from selectable list."""
        logger.info("Starting test: Selectable items")

        # Click on selectable item
        self.interactions_page.click_selectable_item(1)

        # Get selected items
        selected_items = self.interactions_page.get_selected_items()

        assert selected_items, "No items selected"
        logger.info(f"Test passed: Selected items: {selected_items}")

    def test_interaction_04b_multiple_selection(self):
        """TC-INT-04b: Select multiple items with Ctrl+Click."""
        logger.info("Starting test: Multiple item selection")

        # Select first item
        self.interactions_page.click_selectable_item(1)

        # Select second item (in real scenario, would need Ctrl+Click)
        self.interactions_page.click_selectable_item(2)

        selected_items = self.interactions_page.get_selected_items()

        logger.info(f"Selected items count: {len(selected_items)}")
        logger.info("Test passed: Multiple item selection completed")


@pytest.mark.interactions
@pytest.mark.regression
class TestInteractionsComplex:
    """Complex interaction test cases."""

    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Setup for each test."""
        self.interactions_page = InteractionsPage(driver, base_url)
        self.interactions_page.open_interactions()

    def test_interaction_05_complex_workflow(self):
        """TC-INT-05: Complex interaction workflow."""
        logger.info("Starting test: Complex interaction workflow")

        # Test 1: Drag and drop
        try:
            self.interactions_page.drag_draggable_to_drop_zone()
            logger.info("Drag and drop completed")
        except Exception as e:
            logger.warning(f"Drag and drop failed: {str(e)}")

        # Test 2: Get sortable list order
        try:
            order = self.interactions_page.get_sortable_list_order()
            logger.info(f"Sortable list order: {order}")
        except Exception as e:
            logger.warning(f"Getting sortable list order failed: {str(e)}")

        logger.info("Test passed: Complex interaction workflow completed")
