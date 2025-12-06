from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.logger import Logger

logger = Logger.get_logger(__name__)


class FormsPage(BasePage):
    """Page object for DemoQA Forms module."""

    # Locators for practice form
    FIRST_NAME_INPUT = (By.ID, "firstName")
    LAST_NAME_INPUT = (By.ID, "lastName")
    EMAIL_INPUT = (By.ID, "userEmail")
    GENDER_MALE = (By.ID, "gender-radio-1")
    GENDER_FEMALE = (By.ID, "gender-radio-2")
    MOBILE_INPUT = (By.ID, "userNumber")
    DOB_INPUT = (By.ID, "dateOfBirthInput")
    SUBJECT_INPUT = (By.ID, "subjectsInput")
    HOBBIES_SPORTS = (By.ID, "hobbies-checkbox-1")
    HOBBIES_READING = (By.ID, "hobbies-checkbox-2")
    HOBBIES_MUSIC = (By.ID, "hobbies-checkbox-3")
    PICTURE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS_INPUT = (By.ID, "currentAddress")
    STATE_SELECT = (By.ID, "state")
    STATE_INPUT = (By.XPATH, "//input[@id='react-select-3-input']")
    CITY_SELECT = (By.ID, "city")
    CITY_INPUT = (By.XPATH, "//input[@id='react-select-4-input']")
    SUBMIT_BUTTON = (By.ID, "submit")
    SUCCESS_MESSAGE = (By.ID, "example-modal-sizes-title-lg")
    SUCCESS_TABLE = (By.CLASS_NAME, "table-responsive")
    CLOSE_BUTTON = (By.ID, "closeLargeModal")

    def __init__(self, driver, base_url: str):
        """Initialize FormsPage."""
        super().__init__(driver, base_url)

    def open_practice_form(self):
        """Open the practice form page."""
        self.open("/forms")
        logger.info("Opened Practice Form page")

    def fill_first_name(self, first_name: str):
        """Fill first name field."""
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        logger.info(f"Filled first name: {first_name}")

    def fill_last_name(self, last_name: str):
        """Fill last name field."""
        self.type_text(self.LAST_NAME_INPUT, last_name)
        logger.info(f"Filled last name: {last_name}")

    def fill_email(self, email: str):
        """Fill email field."""
        self.type_text(self.EMAIL_INPUT, email)
        logger.info(f"Filled email: {email}")

    def select_gender(self, gender: str):
        """
        Select gender.

        Args:
            gender: 'Male' or 'Female'
        """
        if gender.lower() == "male":
            self.click(self.GENDER_MALE)
            logger.info("Selected gender: Male")
        elif gender.lower() == "female":
            self.click(self.GENDER_FEMALE)
            logger.info("Selected gender: Female")

    def fill_mobile(self, mobile: str):
        """Fill mobile number field."""
        self.type_text(self.MOBILE_INPUT, mobile)
        logger.info(f"Filled mobile: {mobile}")

    def fill_date_of_birth(self, date: str):
        """
        Fill date of birth field.

        Args:
            date: Date string in format DD/MM/YYYY
        """
        self.click(self.DOB_INPUT)
        self.type_text(self.DOB_INPUT, date)
        logger.info(f"Filled date of birth: {date}")

    def fill_subjects(self, subject: str):
        """
        Fill subjects field.

        Args:
            subject: Subject name
        """
        self.click(self.SUBJECT_INPUT)
        self.type_text(self.SUBJECT_INPUT, subject)
        # Select from dropdown
        from selenium.webdriver.common.by import By
        option = (By.XPATH, f"//div[contains(@class, 'option')]//div[contains(text(), '{subject}')]")
        self.click(option, timeout=5)
        logger.info(f"Selected subject: {subject}")

    def select_hobby(self, hobby: str):
        """
        Select hobby checkbox.

        Args:
            hobby: 'Sports', 'Reading', or 'Music'
        """
        if hobby.lower() == "sports":
            self.click(self.HOBBIES_SPORTS)
            logger.info("Selected hobby: Sports")
        elif hobby.lower() == "reading":
            self.click(self.HOBBIES_READING)
            logger.info("Selected hobby: Reading")
        elif hobby.lower() == "music":
            self.click(self.HOBBIES_MUSIC)
            logger.info("Selected hobby: Music")

    def upload_picture(self, file_path: str):
        """
        Upload picture.

        Args:
            file_path: Path to the picture file
        """
        picture_input = self.find(self.PICTURE_INPUT)
        if picture_input:
            picture_input.send_keys(file_path)
            logger.info(f"Uploaded picture: {file_path}")

    def fill_current_address(self, address: str):
        """Fill current address field."""
        self.type_text(self.CURRENT_ADDRESS_INPUT, address)
        logger.info(f"Filled current address: {address}")

    def select_state(self, state: str):
        """
        Select state from dropdown.

        Args:
            state: State name
        """
        self.click(self.STATE_SELECT)
        self.type_text(self.STATE_INPUT, state)
        from selenium.webdriver.common.by import By
        option = (By.XPATH, f"//div[contains(@class, 'option')]//div[contains(text(), '{state}')]")
        self.click(option, timeout=5)
        logger.info(f"Selected state: {state}")

    def select_city(self, city: str):
        """
        Select city from dropdown.

        Args:
            city: City name
        """
        self.click(self.CITY_SELECT)
        self.type_text(self.CITY_INPUT, city)
        from selenium.webdriver.common.by import By
        option = (By.XPATH, f"//div[contains(@class, 'option')]//div[contains(text(), '{city}')]")
        self.click(option, timeout=5)
        logger.info(f"Selected city: {city}")

    def submit_form(self):
        """Submit the form."""
        self.scroll_to_element(self.SUBMIT_BUTTON)
        self.click(self.SUBMIT_BUTTON)
        logger.info("Submitted form")

    def is_success_message_displayed(self) -> bool:
        """Check if success message is displayed."""
        result = self.is_displayed(self.SUCCESS_MESSAGE, timeout=5)
        logger.info(f"Success message displayed: {result}")
        return result

    def get_success_message_text(self) -> str:
        """Get the success message text."""
        text = self.get_text(self.SUCCESS_MESSAGE)
        logger.info(f"Success message text: {text}")
        return text

    def get_submitted_data_table(self) -> str:
        """Get the submitted data table content."""
        table_text = self.get_text(self.SUCCESS_TABLE)
        logger.info(f"Retrieved submitted data table")
        return table_text

    def close_success_modal(self):
        """Close the success modal."""
        self.click(self.CLOSE_BUTTON)
        logger.info("Closed success modal")
