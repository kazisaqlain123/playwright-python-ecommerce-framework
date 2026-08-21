import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.data_reader import read_json


user_data = read_json("users.json")


@pytest.mark.regression
def test_login_with_invalid_credentials(page: Page):
    invalid_user = user_data["invalid_user"]

    home_page = HomePage(page)
    login_page = LoginPage(page)

    home_page.open()
    home_page.go_to_login_page()

    login_page.verify_login_page_is_open()

    login_page.login(
        email=invalid_user["email"],
        password=invalid_user["password"]
    )

    login_page.verify_invalid_login_message()