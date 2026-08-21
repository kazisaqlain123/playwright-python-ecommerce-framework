from playwright.sync_api import Page, expect


class SignupPage:

    def __init__(self, page: Page):
        self.page = page

        self.new_user_heading = page.get_by_role(
            "heading",
            name="New User Signup!",
            exact=True
        )

        self.name_input = page.locator(
            '[data-qa="signup-name"]'
        )

        self.email_input = page.locator(
            '[data-qa="signup-email"]'
        )

        self.signup_button = page.locator(
            '[data-qa="signup-button"]'
        )

        self.account_information_heading = page.get_by_role(
            "heading",
            name="Enter Account Information",
            exact=True
        )

        self.mr_title_radio = page.locator("#id_gender1")
        self.mrs_title_radio = page.locator("#id_gender2")

        self.password_input = page.locator('[data-qa="password"]')
        self.day_dropdown = page.locator('[data-qa="days"]')
        self.month_dropdown = page.locator('[data-qa="months"]')
        self.year_dropdown = page.locator('[data-qa="years"]')

        self.newsletter_checkbox = page.locator("#newsletter")
        self.offers_checkbox = page.locator("#optin")

        self.first_name_input = page.locator('[data-qa="first_name"]')
        self.last_name_input = page.locator('[data-qa="last_name"]')
        self.company_input = page.locator('[data-qa="company"]')
        self.address_input = page.locator('[data-qa="address"]')
        self.address2_input = page.locator('[data-qa="address2"]')
        self.country_dropdown = page.locator('[data-qa="country"]')
        self.state_input = page.locator('[data-qa="state"]')
        self.city_input = page.locator('[data-qa="city"]')
        self.zipcode_input = page.locator('[data-qa="zipcode"]')
        self.mobile_input = page.locator('[data-qa="mobile_number"]')

        self.create_account_button = page.locator(
            '[data-qa="create-account"]'
        )
    def verify_signup_form_is_visible(self):
        expect(self.new_user_heading).to_be_visible()

    def start_signup(self, name: str, email: str):
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.signup_button.click()

    def verify_account_information_form_is_visible(self):
        expect(
            self.account_information_heading
        ).to_be_visible()

    def complete_account_information(
            self,
            user: dict[str, str]
    ):
        if user["title"] == "Mr":
            self.mr_title_radio.check()
        elif user["title"] == "Mrs":
            self.mrs_title_radio.check()
        else:
            raise ValueError("Title must be Mr or Mrs")

        self.password_input.fill(user["password"])

        self.day_dropdown.select_option(user["day"])
        self.month_dropdown.select_option(user["month"])
        self.year_dropdown.select_option(user["year"])

        self.newsletter_checkbox.check()
        self.offers_checkbox.check()

        self.first_name_input.fill(user["first_name"])
        self.last_name_input.fill(user["last_name"])
        self.company_input.fill(user["company"])
        self.address_input.fill(user["address"])
        self.address2_input.fill(user["address2"])

        self.country_dropdown.select_option(user["country"])

        self.state_input.fill(user["state"])
        self.city_input.fill(user["city"])
        self.zipcode_input.fill(user["zipcode"])
        self.mobile_input.fill(user["mobile_number"])

        self.create_account_button.click()