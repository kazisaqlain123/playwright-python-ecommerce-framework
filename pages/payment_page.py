import re

from playwright.sync_api import Page, expect


class PaymentPage:

    def __init__(self, page: Page):
        self.page = page

        self.payment_heading = page.get_by_role(
            "heading",
            name="Payment",
            exact=True
        )

        self.name_on_card_input = page.locator(
            '[data-qa="name-on-card"]'
        )

        self.card_number_input = page.locator(
            '[data-qa="card-number"]'
        )

        self.cvc_input = page.locator(
            '[data-qa="cvc"]'
        )

        self.expiry_month_input = page.locator(
            '[data-qa="expiry-month"]'
        )

        self.expiry_year_input = page.locator(
            '[data-qa="expiry-year"]'
        )

        self.pay_button = page.locator(
            '[data-qa="pay-button"]'
        )

    def verify_payment_page_is_open(self):
        expect(self.page).to_have_url(
            re.compile(r".*/payment")
        )

        expect(self.payment_heading).to_be_visible()

    def enter_payment_details(
        self,
        payment_data: dict[str, str]
    ):
        self.name_on_card_input.fill(
            payment_data["name_on_card"]
        )

        self.card_number_input.fill(
            payment_data["card_number"]
        )

        self.cvc_input.fill(
            payment_data["cvc"]
        )

        self.expiry_month_input.fill(
            payment_data["expiry_month"]
        )

        self.expiry_year_input.fill(
            payment_data["expiry_year"]
        )

    def pay_and_confirm_order(self):
        expect(self.pay_button).to_be_visible()
        self.pay_button.click()