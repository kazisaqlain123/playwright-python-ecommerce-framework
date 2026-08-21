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