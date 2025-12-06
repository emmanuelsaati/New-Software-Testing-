import pytest
import yaml
import os
import csv
from datetime import datetime
from utils.driver_factory import DriverFactory
from utils.logger import Logger
from pages.base_page import BasePage

logger = Logger.get_logger(__name__)


def pytest_addoption(parser):
    """Add custom command line options."""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use: chrome or firefox"
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help="Base URL for tests"
    )


@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture to provide WebDriver instance.

    Yields:
        WebDriver instance
    """
    # Get configuration
    config = load_config()

    # Override with command line options
    browser = request.config.getoption("--browser") or config.get("browser", "chrome")
    headless = request.config.getoption("--headless") or config.get("headless", False)

    # Create driver
    driver_instance = DriverFactory.get_driver(browser=browser, headless=headless)

    logger.info(f"Driver fixture created for test: {request.node.name}")

    yield driver_instance

    # Cleanup
    driver_instance.quit()
    logger.info(f"Driver fixture closed for test: {request.node.name}")


@pytest.fixture(scope="function")
def base_url(request):
    """
    Fixture to provide base URL.

    Returns:
        Base URL
    """
    config = load_config()
    url = request.config.getoption("--base-url") or config.get("base_url", "https://demoqa.com")
    logger.info(f"Base URL: {url}")
    return url


@pytest.fixture(scope="function")
def wait_timeout(request):
    """
    Fixture to provide wait timeout.

    Returns:
        Timeout in seconds
    """
    config = load_config()
    timeout = config.get("explicit_wait", 10)
    return timeout


def load_config():
    """
    Load configuration from config.yaml.

    Returns:
        Configuration dictionary
    """
    config_file = "config.yaml"
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = yaml.safe_load(f) or {}
    else:
        config = {}
        logger.warning(f"Configuration file {config_file} not found, using defaults")

    return config


def read_csv_data(file_path: str) -> list:
    """
    Read test data from CSV file.

    Args:
        file_path: Path to CSV file

    Returns:
        List of dictionaries representing rows
    """
    data = []
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)
        logger.info(f"Loaded {len(data)} rows from {file_path}")
    else:
        logger.warning(f"Test data file {file_path} not found")

    return data


@pytest.fixture
def forms_test_data():
    """Fixture to provide forms test data."""
    return read_csv_data("data/forms_test_data.csv")


def pytest_runtest_makereport(item, call):
    """
    Hook to capture screenshots on test failure.
    """
    if call.when == "call":
        if call.excinfo is not None:
            # Test failed
            driver = item.funcargs.get("driver")
            if driver:
                try:
                    page = BasePage(driver, "https://demoqa.com")
                    screenshot_path = page.screenshot(f"failure_{item.name}")
                    logger.error(f"Test failed. Screenshot saved: {screenshot_path}")

                    # Attach screenshot to Allure report
                    try:
                        import allure
                        with open(screenshot_path, "rb") as f:
                            allure.attach(
                                f.read(),
                                name=f"{item.name}_screenshot",
                                attachment_type=allure.attachment_type.PNG
                            )
                    except ImportError:
                        pass

                except Exception as e:
                    logger.error(f"Failed to capture screenshot: {str(e)}")


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Setup test environment directories."""
    directories = [
        "tests_output",
        "tests_output/screenshots",
        "tests_output/logs",
        "tests_output/allure-results"
    ]

    for directory in directories:
        os.makedirs(directory, exist_ok=True)

    logger.info("Test environment setup completed")
