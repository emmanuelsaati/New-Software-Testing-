# Selenium Automation Testing Framework for DemoQA

A comprehensive Python-based Selenium automation testing framework using the Page Object Model (POM) design pattern to test the DemoQA website (https://demoqa.com/).

## 📋 Overview

This project implements a team-based automation testing framework targeting three main modules of DemoQA:
- **Forms**: User registration and form validation
- **Widgets**: Date pickers, sliders, accordions, tooltips, and progress bars
- **Interactions**: Drag and drop, sortable lists, resizable elements, and more

**Key Features:**
- ✅ Page Object Model (POM) architecture
- ✅ Data-driven testing with CSV support
- ✅ Allure reporting with screenshots on failure
- ✅ CI/CD integration with GitHub Actions
- ✅ Headless browser support for CI environments
- ✅ Comprehensive logging and error handling
- ✅ Cross-browser support (Chrome, Firefox)
- ✅ PEP8 compliant code

## 🎯 Project Requirements

### Functional Requirements
- **FR-001**: Framework setup with Python 3.9+ and Selenium WebDriver
- **FR-002**: Page Object Model implementation for each page/widget
- **FR-003**: Tests for Forms, Widgets, and Interactions modules (minimum 5 tests per module)
- **FR-004**: Data-driven testing for Forms module using CSV
- **FR-005**: Test reporting with Allure and screenshot attachments
- **FR-006**: CLI with configurable options via config.yaml
- **FR-007**: GitHub Actions CI integration
- **FR-008**: Independent, modular test cases

### Non-Functional Requirements
- **NFR-001**: PEP8 style compliance
- **NFR-002**: Reusable components and utilities
- **NFR-003**: Optimized test execution time
- **NFR-004**: Explicit waits and reliable test execution
- **NFR-005**: Cross-platform compatibility (Linux, Windows)
- **NFR-006**: No hardcoded credentials

## 📁 Project Structure

```
demoqa-automation/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── pytest.ini                         # pytest configuration
├── config.yaml                        # Application configuration
├── conftest.py                        # pytest fixtures and hooks
├── .gitignore                         # Git ignore rules
│
├── pages/                             # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py                   # Base page class with common methods
│   ├── forms_page.py                  # Forms module page object
│   ├── widgets_page.py                # Widgets module page object
│   └── interactions_page.py           # Interactions module page object
│
├── tests/                             # Test modules
│   ├── __init__.py
│   ├── test_forms.py                  # Forms test suite
│   ├── test_widgets.py                # Widgets test suite
│   └── test_interactions.py           # Interactions test suite
│
├── utils/                             # Utility modules
│   ├── __init__.py
│   ├── driver_factory.py              # WebDriver factory
│   ├── logger.py                      # Custom logging utility
│   └── helpers.py                     # Helper utilities (wait, retry)
│
├── data/                              # Test data
│   └── forms_test_data.csv            # Test data for data-driven tests
│
├── tests_output/                      # Test execution outputs (generated)
│   ├── screenshots/                   # Failure screenshots
│   ├── logs/                          # Test execution logs
│   └── allure-results/                # Allure report data
│
└── .github/
    └── workflows/
        └── ci.yml                     # GitHub Actions CI workflow
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Chrome or Firefox browser installed
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd demoqa-automation
   ```

2. **Create virtual environment**
   ```bash
   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Edit `config.yaml` to customize your test environment:

```yaml
base_url: https://demoqa.com
browser: chrome                # Options: chrome, firefox
headless: false               # Set to true for headless mode
implicit_wait: 5
explicit_wait: 10
screenshot_on_failure: true
test_data_path: data/forms_test_data.csv
```

## ▶️ Running Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run specific test module
```bash
pytest tests/test_forms.py -v
pytest tests/test_widgets.py -v
pytest tests/test_interactions.py -v
```

### Run tests with specific marker
```bash
pytest -m forms -v              # Run all forms tests
pytest -m widgets -v            # Run all widgets tests
pytest -m interactions -v       # Run all interactions tests
pytest -m positive -v           # Run all positive scenario tests
pytest -m negative -v           # Run all negative scenario tests
pytest -m smoke -v              # Run smoke tests
```

### Run specific test
```bash
pytest tests/test_forms.py::TestFormsPositive::test_form_01_valid_submission -v
```

### Run tests in headless mode
```bash
pytest tests/ --headless -v
```

### Run tests with specific browser
```bash
pytest tests/ --browser firefox -v
```

### Generate Allure report
```bash
# Run tests and generate Allure data
pytest tests/ --alluredir=tests_output/allure-results -v

# Generate HTML report
allure generate tests_output/allure-results --clean -o allure-report

# Serve Allure report in browser
allure serve tests_output/allure-results
```

## 📊 Test Coverage

### Forms Module (test_forms.py)
- **TC-FORM-01**: Valid form submission
- **TC-FORM-02**: All fields filled submission
- **TC-FORM-03**: Male gender selection
- **TC-FORM-04**: Invalid email validation
- **TC-FORM-05**: Invalid mobile number validation
- **TC-FORM-06**: Maximum length name handling
- **Data-driven tests**: Multiple scenarios from CSV

### Widgets Module (test_widgets.py)
- **TC-WID-01**: Date picker selection
- **TC-WID-02**: Slider value changes
- **TC-WID-02b**: Slider minimum value
- **TC-WID-02c**: Slider maximum value
- **TC-WID-03**: Accordion expand/collapse
- **TC-WID-03b**: Accordion content display
- **TC-WID-04**: Tooltip hover display
- **TC-WID-05**: Multiple widget interactions

### Interactions Module (test_interactions.py)
- **TC-INT-01**: Sortable drag and drop
- **TC-INT-02**: Drag and drop to drop zone
- **TC-INT-02b**: Drop zone text verification
- **TC-INT-03**: Element resize
- **TC-INT-04**: Selectable items
- **TC-INT-04b**: Multiple item selection
- **TC-INT-05**: Complex interaction workflow

## 🔧 Key Components

### BasePage (pages/base_page.py)
Base class providing common methods for all page objects:
- `open(url)` - Open a URL
- `find(locator)` - Find an element
- `click(locator)` - Click an element
- `type_text(locator, text)` - Type text into element
- `get_text(locator)` - Get element text
- `is_displayed(locator)` - Check element visibility
- `hover(locator)` - Hover over element
- `double_click(locator)` - Double-click element
- `right_click(locator)` - Right-click element
- `drag_and_drop(source, target)` - Drag and drop elements
- `screenshot(name)` - Take screenshot
- `wait_for_element_visible(locator)` - Wait for visibility
- And many more...

### DriverFactory (utils/driver_factory.py)
Creates and manages WebDriver instances:
- Supports Chrome and Firefox
- Headless mode support
- Automatic driver management with webdriver-manager
- Browser options configuration

### Logger (utils/logger.py)
Custom logging utility:
- File and console logging
- DEBUG and INFO level logging
- Timestamped log files

### WaitHelper (utils/helpers.py)
Helper utilities for common operations:
- Explicit waits for element visibility/clickability
- Text-in-element waits
- URL change waits
- Retry operations with configurable attempts

## 📝 Data-Driven Testing

The framework supports data-driven testing using CSV files. Test data for Forms is located in `data/forms_test_data.csv`:

```csv
first_name,last_name,email,gender,mobile,date_of_birth,subject,hobby,address,state,city,expected_result
John,Doe,john.doe@example.com,Male,9876543210,01/01/1990,Math,Sports,123 Main Street,NCR,Delhi,success
Jane,Smith,jane.smith@example.com,Female,8765432109,15/05/1995,English,Reading,456 Oak Avenue,Rajasthan,Jaipur,success
...
```

The `test_form_data_driven_submission` test iterates through all rows and executes the test with each data set.

## 📊 Test Reporting

### Allure Reports
Tests are integrated with Allure reporting, providing:
- Test execution summary
- Pass/fail statistics
- Detailed test steps
- Screenshots on failure
- Test execution timeline

### Screenshots
Screenshots are automatically captured:
- On test failure (via pytest hook)
- Manually via `page.screenshot(name)`
- Saved to `tests_output/screenshots/`
- Attached to Allure reports

### Logs
Test execution logs are saved to `tests_output/logs/`:
- Timestamped log files
- DEBUG level file logging
- INFO level console logging

## 🔄 CI/CD Integration

### GitHub Actions Workflow
The `.github/workflows/ci.yml` file defines the CI pipeline:
- Runs on push to main/develop branches
- Runs on pull requests
- Tests on Python 3.9, 3.10, 3.11
- Generates Allure reports
- Uploads artifacts
- Deploys reports to GitHub Pages

### Running in CI
Tests run in headless mode in CI environments:
```bash
pytest tests/ --headless --alluredir=tests_output/allure-results -v
```

## 🎨 Code Style and Conventions

This project follows PEP8 standards:
- 4-space indentation
- Maximum line length of 100 characters (where practical)
- Clear naming conventions:
  - `test_` prefix for test methods
  - `_locator` suffix for locators
  - `_element` suffix for element references

Example:
```python
@pytest.mark.forms
@pytest.mark.positive
def test_form_01_valid_submission(self):
    """Test description - imperative style."""
    # Test implementation
```

## 🐛 Troubleshooting

### Tests fail with "Element not found"
- Verify the element locators in page objects
- Check if the website structure has changed
- Use browser developer tools to inspect elements
- Ensure proper waits are in place

### Headless mode failures
- Some elements may behave differently in headless mode
- Test locally in headless mode before CI
- Increase wait times if needed
- Check browser compatibility

### Timeout errors
- Increase explicit wait timeout in config.yaml
- Verify internet connection and website availability
- Check browser performance
- Review page load time

### Screenshot not captured on failure
- Ensure `tests_output/` directory exists
- Check file permissions
- Verify screenshot directory is writable

## 📚 Additional Resources

- [Selenium Documentation](https://selenium.dev/documentation/)
- [pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- [Page Object Model Pattern](https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/)
- [DemoQA Website](https://demoqa.com/)

## 📋 Deliverables

As per the PRD, this project includes:
- ✅ Source code repository with full framework
- ✅ README with setup and usage instructions
- ✅ Test data files (CSV format)
- ✅ Allure test reports and screenshots
- ✅ Comprehensive documentation
- ✅ GitHub Actions CI/CD integration
- ✅ Minimum 15 test cases (5+ per module)
- ✅ Data-driven tests implementation

## 👥 Team

- **Project Lead**: Emmanuel Saati
- **Developers/QA Engineers**: Student group members
- **Reviewer**: Teaching Assistant / Peers

## 📄 License

This project is created for academic purposes.

## 🤝 Contributing

1. Create a feature branch from `develop`
2. Make your changes following the code style guidelines
3. Add/update tests as needed
4. Submit a pull request with clear descriptions
5. Ensure CI pipeline passes

## 📞 Support

For issues or questions, please create an issue in the repository or contact the project lead.

---

**Last Updated**: December 2024  
**Framework Version**: 1.0.0
