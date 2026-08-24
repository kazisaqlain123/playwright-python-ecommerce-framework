import re

import pytest
from playwright.sync_api import BrowserContext
from pytest_html import extras
from pytest_metadata.plugin import metadata_key
from pytest_playwright.pytest_playwright import CreateContextCallback

from utils.account_api import create_account, delete_account
from utils.data_generator import generate_unique_email
from utils.data_reader import read_json


GOOGLE_AD_URL = re.compile(
    r"https?://[^/]*(?:"
    r"doubleclick\.net|"
    r"googlesyndication\.com|"
    r"googleadservices\.com"
    r")/.*"
)


def pytest_configure(config):
    metadata = config.stash[metadata_key]

    metadata["Project"] = (
        "Playwright Python E-Commerce Framework"
    )
    metadata["Application"] = "Automation Exercise"

    metadata["Test Stage"] = (
        "Stage 3 - Reporting and Artifacts"
    )


def pytest_html_report_title(report):
    report.title = (
        "Playwright E-Commerce Test Automation Report"
    )


@pytest.fixture
def context(
    new_context: CreateContextCallback
) -> BrowserContext:
    context = new_context()

    context.route(
        GOOGLE_AD_URL,
        lambda route: route.abort()
    )

    return context


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {
            "width": 1440,
            "height": 900
        }
    }


@pytest.fixture
def registered_user() -> dict[str, str]:
    user = read_json(
        "users.json"
    )["registration_user"].copy()

    user["email"] = generate_unique_email()

    create_account(user)

    try:
        yield user
    finally:
        delete_account(
            email=user["email"],
            password=user["password"]
        )


@pytest.fixture
def registered_users() -> list[dict[str, str]]:
    users = []

    try:
        for user_number in range(1, 3):
            user = read_json(
                "users.json"
            )["registration_user"].copy()

            user["name"] = (
                f"Context User {user_number}"
            )
            user["first_name"] = "Context"
            user["last_name"] = (
                f"User {user_number}"
            )
            user["email"] = generate_unique_email()

            create_account(user)
            users.append(user)

        yield users

    finally:
        for user in users:
            delete_account(
                email=user["email"],
                password=user["password"]
            )