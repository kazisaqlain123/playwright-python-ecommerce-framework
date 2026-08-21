import pytest
from playwright.sync_api import Page

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_with_valid_credentials_and_logout(
    page: Page,
    registered_user: dict[str, str]
):
    home_page = HomePage(page)
    login_page = LoginPage(page)
    account_page = AccountPage(page)

    home_page.open()
    home_page.go_to_login_page()

    login_page.verify_login_page_is_open()

    login_page.login(
        email=registered_user["email"],
        password=registered_user["password"]
    )

    account_page.verify_logged_in_as(
        registered_user["name"]
    )

    account_page.logout()

    login_page.verify_login_page_is_open()