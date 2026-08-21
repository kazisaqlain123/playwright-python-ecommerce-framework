from playwright.sync_api import Page, expect


class AccountPage:

    def __init__(self, page: Page):
        self.page = page

        self.account_created_heading = page.locator(
            '[data-qa="account-created"]'
        )

        self.continue_button = page.locator(
            '[data-qa="continue-button"]'
        )

        self.delete_account_link = page.get_by_role(
            "link",
            name="Delete Account"
        )

        self.account_deleted_heading = page.locator(
            '[data-qa="account-deleted"]'
        )

        self.logout_link = page.locator(
            'a[href="/logout"]'
        )

    def verify_account_was_created(self):
        expect(self.account_created_heading).to_be_visible()

    def continue_after_creation(self):
        self.continue_button.click()

    def verify_logged_in_as(self, name: str):
        logged_in_message = self.page.get_by_text(
            f"Logged in as {name}",
            exact=True
        )

        expect(logged_in_message).to_be_visible()

    def logout(self):
        expect(self.logout_link).to_be_visible()
        self.logout_link.click()

    def delete_account(self):
        self.delete_account_link.click()

    def verify_account_was_deleted(self):
        expect(self.account_deleted_heading).to_be_visible()

