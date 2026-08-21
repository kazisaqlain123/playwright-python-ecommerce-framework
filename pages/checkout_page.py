import re

from playwright.sync_api import Page, expect


class CheckoutPage:

    def __init__(self, page: Page):
        self.page = page

        self.address_details_heading = page.get_by_text(
            "Address Details",
            exact=True
        )

        self.review_order_heading = page.get_by_text(
            "Review Your Order",
            exact=True
        )

        self.delivery_address = page.locator(
            "#address_delivery"
        )

        self.billing_address = page.locator(
            "#address_invoice"
        )

        self.order_comment_input = page.locator(
            'textarea[name="message"]'
        )

        self.place_order_link = page.get_by_role(
            "link",
            name="Place Order",
            exact=True
        )

    def verify_checkout_page_is_open(self):
        expect(self.page).to_have_url(
            re.compile(r".*/checkout")
        )

        expect(self.address_details_heading).to_be_visible()
        expect(self.review_order_heading).to_be_visible()

    def verify_delivery_and_billing_addresses(
        self,
        user: dict[str, str]
    ):
        expected_values = [
            f'{user["title"]}. {user["first_name"]} {user["last_name"]}',
            user["company"],
            user["address"],
            user["address2"],
            user["city"],
            user["state"],
            user["zipcode"],
            user["country"],
            user["mobile_number"]
        ]

        for expected_value in expected_values:
            expect(self.delivery_address).to_contain_text(
                expected_value
            )

            expect(self.billing_address).to_contain_text(
                expected_value
            )

    def add_order_comment(self, comment: str):
        self.order_comment_input.fill(comment)

    def place_order(self):
        expect(self.place_order_link).to_be_visible()
        self.place_order_link.click()