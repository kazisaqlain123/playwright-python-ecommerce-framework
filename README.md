# Playwright Python E-Commerce Test Automation Framework

[![Playwright Tests](https://github.com/kazisaqlain123/playwright-python-ecommerce-framework/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/kazisaqlain123/playwright-python-ecommerce-framework/actions/workflows/playwright-tests.yml)

A portfolio-ready test automation framework built with Python, Playwright, and Pytest. It automates realistic UI and API-assisted workflows on the Automation Exercise e-commerce practice website.

## Application Under Test

[Automation Exercise](https://www.automationexercise.com/)

## Technologies

- Python
- Playwright
- Pytest
- Requests
- Page Object Model
- JSON and CSV test data
- Git and GitHub
- Pytest HTML and Pytest Metadata
- GitHub Actions

## Automated Test Scenarios

- Verify that the home page opens successfully
- Verify login with invalid credentials
- Search for multiple products using CSV data
- Add a searched product to the shopping cart
- Register a new user and delete the account after verification
- Create test accounts through the API
- Log in with valid credentials and log out
- Complete checkout with delivery and billing address validation
- Submit payment details and verify order confirmation
- Download and verify the generated invoice
- Submit the Contact Us form with a file attachment and confirmation dialog
- Verify that two browser contexts maintain isolated user sessions

The suite collects 11 tests. GitHub Actions executes the framework across Chromium, Firefox, and WebKit. Product search is parameterized with three CSV data rows.

## Framework Features

- Page Object Model architecture
- Reusable Pytest fixtures
- Central browser-context configuration
- API-assisted test setup and cleanup
- Unique email generation for independent test execution
- Guaranteed account cleanup using fixture teardown
- JSON-based registration and payment data
- CSV-based product-search data
- Pytest parameterization
- Smoke, regression, and end-to-end markers
- File upload and JavaScript dialog handling
- Network-response validation
- Download handling and invoice verification
- Multiple isolated browser contexts
- Optional cookie-consent handling
- Stable Playwright locators and assertions
- Automatic self-contained HTML reporting
- Custom report title and environment metadata
- Screenshots captured on failure
- Videos and Playwright traces retained on failure
- Failure evidence for multiple managed browser contexts
- Third-party advertisement blocking for stable execution
- Controlled retry for delayed product-search responses

## Project Structure

```text
playwright-python-ecommerce-framework/
├── .github/
│   └── workflows/
│       └── playwright-tests.yml
├── pages/
│   ├── account_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── contact_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── order_confirmation_page.py
│   ├── payment_page.py
│   ├── products_page.py
│   └── signup_page.py
├── tests/
│   ├── test_browser_contexts.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   ├── test_contact.py
│   ├── test_home_page.py
│   ├── test_login.py
│   ├── test_products.py
│   ├── test_registration.py
│   └── test_valid_login.py
├── test_data/
│   ├── contact_attachment.txt
│   ├── payment.json
│   ├── products.csv
│   └── users.json
├── utils/
│   ├── account_api.py
│   ├── data_generator.py
│   └── data_reader.py
├── reports/                # Generated HTML report, ignored by Git
├── test-results/         # Generated failure evidence, ignored by Git
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/kazisaqlain123/playwright-python-ecommerce-framework.git
cd playwright-python-ecommerce-framework
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies and Playwright browsers:

```bash
python -m pip install -r requirements.txt
python -m playwright install
```

## Running Tests

Run the complete test suite:

```bash
python -m pytest
```

Run tests with a visible browser:

```bash
python -m pytest --headed
```

Run only smoke tests:

```bash
python -m pytest -m smoke
```

Run only regression tests:

```bash
python -m pytest -m regression
```

Run only end-to-end tests:

```bash
python -m pytest -m e2e
```

Run a specific test file:

```bash
python -m pytest tests/test_checkout.py --headed -v --tb=short
```
## Reports and Failure Evidence

Every test execution automatically generates a self-contained HTML report:

```text
reports/report.html
```

Open the report on macOS:

```bash
open reports/report.html
```

The report contains project details, application details, the base URL, environment information, test results, and execution durations.

When a test fails, the framework automatically saves evidence under `test-results/`:

- Screenshot at the point of failure
- Browser video
- Playwright trace

Open a saved trace using:

```bash
python -m playwright show-trace path/to/trace.zip
```

The `reports/` and `test-results/` directories are generated during execution and excluded from Git.
## Test Data and Cleanup

Registration and payment details are stored in JSON files, while product-search inputs are stored in CSV. Unique email addresses are generated during execution to prevent conflicts between repeated runs.

Tests that require an existing account create it through the Automation Exercise API. Pytest fixture teardown deletes temporary accounts even when a UI assertion fails.

All payment values are fictional and are used only on the practice website.

## Current Status

Stage 4 is complete with automated cross-browser execution through GitHub Actions.

The CI pipeline runs the test suite on Chromium, Firefox, and WebKit for pushes and pull requests targeting the `main` branch. All three browser jobs have completed successfully.

The framework now includes advanced e-commerce workflows, API-assisted setup and cleanup, isolated browser contexts, HTML reporting, custom metadata, failure screenshots, retained videos, Playwright traces, cross-browser CI, and uploaded test artifacts.

## Continuous Integration

The GitHub Actions workflow:

- Runs automatically for pushes and pull requests targeting `main`
- Uses Ubuntu and Python 3.13
- Executes Chromium, Firefox, and WebKit as separate matrix jobs
- Installs each Playwright browser with its required system dependencies
- Uploads a self-contained HTML report for every browser
- Uploads screenshots, videos, and traces when a job fails
- Retains uploaded artifacts for 14 days
- Prevents one browser failure from cancelling the remaining browser jobs

The workflow is located at:

```text
.github/workflows/playwright-tests.yml

## Known Limitation

The public practice website can behave differently in headless execution. For the Contact Us workflow, the test verifies the successful POST response and returned confirmation message because the visible success container can remain empty even when the server returns HTTP 200 with the expected content.

## Roadmap

### Stage 4: Continuous Integration

- GitHub Actions execution after pushes and pull requests
- Chromium, Firefox, and WebKit coverage
- Uploaded HTML reports and failure artifacts
- GitHub Actions status badge