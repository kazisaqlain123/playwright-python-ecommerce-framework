import re

from playwright.sync_api import Page, expect


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_table = page.locator(
            "#cart_info"
        )

        self.product_names = page.locator(
            "#cart_info .cart_description h4 a"
        )

    def verify_cart_page_is_open(self):
        expect(self.page).to_have_url(
            re.compile(r".*/view_cart")
        )

        expect(self.cart_table).to_be_visible()

    def verify_product_is_in_cart(self, product_name: str):
        matching_product = self.product_names.filter(
            has_text=product_name
        )

        expect(matching_product).to_be_visible()