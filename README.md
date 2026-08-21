# Playwright Python E-Commerce Test Automation Framework

A portfolio test automation framework built with Python, Playwright and Pytest. It automates essential workflows on the Automation Exercise e-commerce practice website.

## Application Under Test

[Automation Exercise](https://www.automationexercise.com/)

## Technologies

- Python
- Playwright
- Pytest
- Page Object Model
- JSON test data
- CSV test data
- Git and GitHub

## Automated Test Scenarios

- Verify the home page opens successfully
- Verify login with invalid credentials
- Search for multiple products using CSV data
- Add a searched product to the shopping cart
- Verify the selected product appears in the cart

## Framework Features

- Page Object Model architecture
- Reusable Pytest fixtures
- Central browser-context configuration
- JSON-based login data
- CSV-based product-search data
- Pytest parameterization
- Smoke and regression markers
- Optional cookie-consent handling
- Stable Playwright locators and assertions

## Project Structure

```text
playwright-python-ecommerce-framework/
├── pages/
│   ├── home_page.py
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
├── tests/
│   ├── test_home_page.py
│   ├── test_login.py
│   ├── test_products.py
│   └── test_cart.py
├── test_data/
│   ├── users.json
│   └── products.csv
├── utils/
│   └── data_reader.py
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

Install the dependencies:

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

Run a specific test file:

```bash
python -m pytest tests/test_cart.py --headed
```

## Current Status

Stage 1 is complete with six passing Chromium tests.

Future stages will add registration, checkout, file upload, invoice download, reporting, screenshots, videos, traces, cross-browser execution and GitHub Actions.