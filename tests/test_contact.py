from pathlib import Path
from utils.data_generator import generate_unique_email
import pytest
from playwright.sync_api import Page

from pages.contact_page import ContactPage
from pages.home_page import HomePage


PROJECT_ROOT = Path(__file__).resolve().parent.parent

ATTACHMENT_PATH = (
    PROJECT_ROOT
    / "test_data"
    / "contact_attachment.txt"
)

@pytest.mark.only_browser("chromium")
@pytest.mark.regression
def test_submit_contact_form_with_attachment(
    page: Page
):

    home_page = HomePage(page)
    contact_page = ContactPage(page)

    home_page.open()
    home_page.go_to_contact_us_page()

    contact_page.verify_contact_page_is_open()

    contact_email = generate_unique_email()
    contact_page.fill_contact_form(
        name="QA Automation User",
        email=contact_email,
        subject="Playwright automation test",
        message="Testing the Contact Us workflow."
    )

    contact_page.upload_attachment(
        ATTACHMENT_PATH
    )

    response_body = (
        contact_page.submit_and_accept_dialog()
    )

    contact_page.verify_submission_response(
        response_body
    )