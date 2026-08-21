import pytest
from playwright.sync_api import Page

from pages.home_page import HomePage


@pytest.mark.smoke
def test_home_page_opens_successfully(page: Page):
    home_page = HomePage(page)

    home_page.open()

    home_page.verify_home_page_is_open()