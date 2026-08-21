from playwright.sync_api import Page, expect


class HomePage:

    def __init__(self, page: Page):
        self.page = page

        self.signup_login_link = page.get_by_role(
            "link",
            name="Signup / Login"
        )

        self.products_link = page.get_by_role(
            "link",
            name="Products"
        )

        self.cart_link = page.get_by_role(
            "link",
            name="Cart"
        )

    def open(self):
        self.page.goto("/")

    def verify_home_page_is_open(self):
        expect(self.page).to_have_title("Automation Exercise")

    def go_to_login_page(self):
        self.signup_login_link.click()