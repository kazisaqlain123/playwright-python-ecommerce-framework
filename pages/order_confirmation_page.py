import re
from pathlib import Path

from playwright.sync_api import Page, expect


class OrderConfirmationPage:

    def __init__(self, page: Page):
        self.page = page

        self.order_placed_heading = page.locator(
            '[data-qa="order-placed"]'
        )

        self.confirmation_message = page.get_by_text(
            "Congratulations! Your order has been confirmed!",
            exact=True
        )
        self.download_invoice_link = page.get_by_role(
            "link",
            name="Download Invoice",
            exact=True
        )

    def verify_order_was_placed(self):
        expect(self.page).to_have_url(
            re.compile(r".*/payment_done/.*")
        )

        expect(self.order_placed_heading).to_be_visible()
        expect(self.confirmation_message).to_be_visible()

    def download_invoice(
            self,
            download_directory: Path
    ) -> Path:
        expect(self.download_invoice_link).to_be_visible()

        with self.page.expect_download() as download_info:
            self.download_invoice_link.click()

        download = download_info.value

        invoice_path = (
                download_directory / download.suggested_filename
        )

        download.save_as(invoice_path)

        return invoice_path