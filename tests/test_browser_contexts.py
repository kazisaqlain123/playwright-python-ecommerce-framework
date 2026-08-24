import pytest
from playwright.sync_api import Page
from pytest_playwright.pytest_playwright import (
    CreateContextCallback
)

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


def login_user(
    page: Page,
    user: dict[str, str]
) -> AccountPage:
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    home_page.open()
    home_page.go_to_login_page()

    login_page.login(
        email=user["email"],
        password=user["password"]
    )

    account_page.verify_logged_in_as(
        user["name"]
    )

    return account_page


@pytest.mark.regression
def test_browser_contexts_keep_sessions_isolated(
    new_context: CreateContextCallback,
    registered_users: list[dict[str, str]]
):
    user_one, user_two = registered_users

    context_one = new_context()
    context_two = new_context()

    page_one = context_one.new_page()
    page_two = context_two.new_page()

    account_page_one = login_user(
        page_one,
        user_one
    )

    account_page_two = login_user(
        page_two,
        user_two
    )

    account_page_one.logout()

    LoginPage(
        page_one
    ).verify_login_page_is_open()

    account_page_two.verify_logged_in_as(
        user_two["name"]
    )