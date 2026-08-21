from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

        self.all_products_heading = page.get_by_role(
            "heading",
            name="All Products",
            exact=True
        )

        self.search_input = page.get_by_role(
            "textbox",
            name="Search Product"
        )

        self.search_button = page.locator(
            "#submit_search"
        )

        self.searched_products_heading = page.get_by_role(
            "heading",
            name="Searched Products",
            exact=True
        )

        self.product_names = page.locator(
            ".features_items .productinfo p"
        )
        self.added_to_cart_message = page.get_by_text(
            "Your product has been added to cart.",
            exact=True
        )

        self.view_cart_link = page.get_by_role(
            "link",
            name="View Cart"
        )

    def verify_products_page_is_open(self):
        expect(self.all_products_heading).to_be_visible()

    def search_for_product(self, product_name: str):
        self.search_input.fill(product_name)
        self.search_button.click()

    def verify_product_is_displayed(self, product_name: str):
        expect(self.searched_products_heading).to_be_visible()

        matching_product = self.product_names.filter(
            has_text=product_name
        )

        expect(matching_product.first).to_be_visible()

    def add_product_to_cart(self, product_name: str):
        product_card = self.page.locator(
            ".productinfo"
        ).filter(
            has_text=product_name
        ).first

        add_to_cart_button = product_card.locator(
            ".add-to-cart"
        )

        expect(add_to_cart_button).to_be_visible()
        add_to_cart_button.click()

        expect(self.added_to_cart_message).to_be_visible()

    def go_to_cart_from_modal(self):
        self.view_cart_link.click()