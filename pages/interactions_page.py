from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

logger = Logger.get_logger(__name__)


class InteractionsPage(BasePage):
    """Page object for DemoQA Interactions module."""

    # Sortable locators
    SORTABLE_LIST_ITEM_1 = (By.XPATH, "//div[@class='list-group-item' and text()='One']")
    SORTABLE_LIST_ITEM_2 = (By.XPATH, "//div[@class='list-group-item' and text()='Two']")
    SORTABLE_LIST_ITEM_3 = (By.XPATH, "//div[@class='list-group-item' and text()='Three']")
    SORTABLE_LIST_ITEM_4 = (By.XPATH, "//div[@class='list-group-item' and text()='Four']")
    SORTABLE_LIST_ITEM_5 = (By.XPATH, "//div[@class='list-group-item' and text()='Five']")
    SORTABLE_LIST_ITEM_6 = (By.XPATH, "//div[@class='list-group-item' and text()='Six']")

    # Selectable locators
    SELECTABLE_ITEM_1 = (By.XPATH, "//ul[@id='selectable']//li[@class='ui-selectee' and text()='Cras justo odio']")
    SELECTABLE_ITEM_2 = (By.XPATH, "//ul[@id='selectable']//li[@class='ui-selectee' and text()='Dapibus ac facilisis in']")
    SELECTABLE_ITEM_3 = (By.XPATH, "//ul[@id='selectable']//li[@class='ui-selectee' and text()='Morbi leo risus']")

    # Draggable/Droppable locators
    DRAGGABLE_ELEMENT = (By.ID, "draggable")
    DROP_ZONE = (By.ID, "droppable")
    DROP_ZONE_TEXT = (By.XPATH, "//div[@id='droppable']/p")

    # Resizable locators
    RESIZABLE_HANDLE = (By.CLASS_NAME, "ui-resizable-handle")
    RESIZABLE_BOX = (By.ID, "resizable")

    # Dynamic Table locators
    TABLE_ROWS = (By.XPATH, "//div[@class='table-responsive']//tr")

    def __init__(self, driver, base_url: str):
        """Initialize InteractionsPage."""
        super().__init__(driver, base_url)

    def open_interactions(self):
        """Open the interactions page."""
        self.open("/interaction")
        logger.info("Opened Interactions page")

    # Sortable methods
    def drag_sortable_item(self, source_item: int, target_item: int):
        """
        Drag a sortable item to another position.

        Args:
            source_item: Source item number (1-6)
            target_item: Target item number (1-6)
        """
        items = {
            1: self.SORTABLE_LIST_ITEM_1,
            2: self.SORTABLE_LIST_ITEM_2,
            3: self.SORTABLE_LIST_ITEM_3,
            4: self.SORTABLE_LIST_ITEM_4,
            5: self.SORTABLE_LIST_ITEM_5,
            6: self.SORTABLE_LIST_ITEM_6,
        }

        source = items.get(source_item)
        target = items.get(target_item)

        if source and target:
            self.drag_and_drop(source, target)
            logger.info(f"Dragged sortable item {source_item} to {target_item}")

    def get_sortable_list_order(self) -> list:
        """
        Get the current order of sortable list items.

        Returns:
            List of item names in current order
        """
        all_items = self.find_elements((By.XPATH, "//div[@class='list-group-item']"))
        order = [item.text for item in all_items]
        logger.info(f"Retrieved sortable list order: {order}")
        return order

    # Selectable methods
    def click_selectable_item(self, item_number: int):
        """
        Click a selectable item.

        Args:
            item_number: Item number (1, 2, or 3)
        """
        items = {
            1: self.SELECTABLE_ITEM_1,
            2: self.SELECTABLE_ITEM_2,
            3: self.SELECTABLE_ITEM_3,
        }

        item = items.get(item_number)
        if item:
            self.click(item)
            logger.info(f"Clicked selectable item {item_number}")

    def get_selected_items(self) -> list:
        """
        Get list of selected items.

        Returns:
            List of selected item texts
        """
        selected = self.find_elements((By.XPATH, "//ul[@id='selectable']//li[@class='ui-selectee ui-selected']"))
        selected_texts = [item.text for item in selected]
        logger.info(f"Retrieved selected items: {selected_texts}")
        return selected_texts

    # Draggable/Droppable methods
    def drag_draggable_to_drop_zone(self):
        """Drag the draggable element to the drop zone."""
        self.drag_and_drop(self.DRAGGABLE_ELEMENT, self.DROP_ZONE)
        logger.info("Dragged draggable element to drop zone")

    def get_drop_zone_text(self) -> str:
        """Get the text in the drop zone."""
        text = self.get_text(self.DROP_ZONE_TEXT)
        logger.info(f"Retrieved drop zone text: {text}")
        return text

    def is_item_dropped(self) -> bool:
        """Check if an item has been dropped in the drop zone."""
        text = self.get_drop_zone_text()
        is_dropped = "Dropped" in text
        logger.info(f"Item dropped: {is_dropped}")
        return is_dropped

    # Resizable methods
    def resize_element(self, width_delta: int, height_delta: int):
        """
        Resize an element by dragging the resize handle.

        Args:
            width_delta: Width change in pixels
            height_delta: Height change in pixels
        """
        handle = self.find(self.RESIZABLE_HANDLE)
        if handle:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).drag_and_drop_by_offset(
                handle, width_delta, height_delta
            ).perform()
            logger.info(f"Resized element by width: {width_delta}, height: {height_delta}")

    def get_element_size(self) -> dict:
        """
        Get the size of a resizable element.

        Returns:
            Dictionary with 'width' and 'height' keys
        """
        element = self.find(self.RESIZABLE_BOX)
        if element:
            size = element.size
            logger.info(f"Retrieved element size: {size}")
            return size
        return {"width": 0, "height": 0}

    # Droppable methods
    def drag_element_within_zone(self, x_offset: int, y_offset: int):
        """
        Drag an element within its container.

        Args:
            x_offset: Horizontal offset in pixels
            y_offset: Vertical offset in pixels
        """
        draggable = self.find(self.DRAGGABLE_ELEMENT)
        if draggable:
            from selenium.webdriver.common.action_chains import ActionChains
            ActionChains(self.driver).drag_and_drop_by_offset(
                draggable, x_offset, y_offset
            ).perform()
            logger.info(f"Dragged element within zone: x={x_offset}, y={y_offset}")
