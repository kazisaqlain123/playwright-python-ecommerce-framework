from playwright.sync_api import (
    Page,
    TimeoutError as PlaywrightTimeoutError,
    expect
)


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

        self.cookie_consent_button = page.locator(
            ".fc-cta-consent"
        )

    def open(self):
        self.page.goto("/")
        self.accept_cookie_consent_if_visible()

    def accept_cookie_consent_if_visible(self):
        try:
            self.cookie_consent_button.wait_for(
                state="visible",
                timeout=3000
            )
        except PlaywrightTimeoutError:
            return

        self.cookie_consent_button.click()

    def verify_home_page_is_open(self):
        expect(self.page).to_have_title("Automation Exercise")

    def go_to_login_page(self):
        self.signup_login_link.click()

    def go_to_products_page(self):
        self.products_link.click()