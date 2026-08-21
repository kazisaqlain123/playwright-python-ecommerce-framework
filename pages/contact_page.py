import re
from pathlib import Path

from playwright.sync_api import Page, expect


class ContactPage:

    def __init__(self, page: Page):
        self.page = page

        self.get_in_touch_heading = page.get_by_role(
            "heading",
            name="Get In Touch",
            exact=True
        )

        self.name_input = page.locator(
            '[data-qa="name"]'
        )

        self.email_input = page.locator(
            '[data-qa="email"]'
        )

        self.subject_input = page.locator(
            '[data-qa="subject"]'
        )

        self.message_input = page.locator(
            '[data-qa="message"]'
        )

        self.upload_input = page.locator(
            'input[name="upload_file"]'
        )

        self.submit_button = page.locator(
            '[data-qa="submit-button"]'
        )


    def verify_contact_page_is_open(self):
        expect(self.page).to_have_url(
            re.compile(r".*/contact_us")
        )

        expect(self.get_in_touch_heading).to_be_visible()

    def fill_contact_form(
        self,
        name: str,
        email: str,
        subject: str,
        message: str
    ):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.message_input.fill(message)

    def upload_attachment(
        self,
        attachment_path: Path
    ):
        self.upload_input.set_input_files(
            attachment_path
        )

    def submit_and_accept_dialog(self) -> str:
        self.page.once(
            "dialog",
            lambda dialog: dialog.accept()
        )

        with self.page.expect_response(
                lambda response: (
                        response.request.method == "POST"
                        and response.url.rstrip("/").endswith(
                    "/contact_us"
                )
                ),
                timeout=30000
        ) as response_info:
            self.submit_button.click()

        response = response_info.value

        assert response.ok, (
            f"Contact form request failed with "
            f"HTTP status {response.status}"
        )

        return response.text()

    def verify_submission_response(
            self,
            response_body: str
    ):
        expected_message = (
            "Success! Your details have been "
            "submitted successfully."
        )

        assert expected_message in response_body, (
            "The Contact Us response did not contain "
            "the expected success message."
        )