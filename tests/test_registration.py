import pytest
from playwright.sync_api import Page

from pages.account_page import AccountPage
from pages.home_page import HomePage
from pages.signup_page import SignupPage
from utils.data_generator import generate_unique_email
from utils.data_reader import read_json


user_data = read_json("users.json")


@pytest.mark.regression
def test_register_new_user(page: Page):
    registration_user = user_data["registration_user"]
    unique_email = generate_unique_email()

    home_page = HomePage(page)
    signup_page = SignupPage(page)
    account_page = AccountPage(page)

    home_page.open()
    home_page.go_to_login_page()

    signup_page.verify_signup_form_is_visible()

    signup_page.start_signup(
        name=registration_user["name"],
        email=unique_email
    )

    signup_page.verify_account_information_form_is_visible()
    signup_page.complete_account_information(registration_user)

    account_page.verify_account_was_created()
    account_page.continue_after_creation()
    account_page.verify_logged_in_as(registration_user["name"])

    account_page.delete_account()
    account_page.verify_account_was_deleted()