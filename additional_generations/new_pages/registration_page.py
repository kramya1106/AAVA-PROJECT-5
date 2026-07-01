"""
Page object for user registration page.
This page object represents the registration form with all required fields for user account creation.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class RegistrationPage(BasePageObject):
    """Page object for the user registration page."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.username_input = "[data-testid='username'], #username, input[name='username']"
        self.elements.email_input = "[data-testid='email'], #email, input[type='email'], input[name='email']"
        self.elements.password_input = "[data-testid='password'], #password, input[type='password'][name='password']"
        self.elements.confirm_password_input = "[data-testid='confirm-password'], #confirmPassword, input[name='confirmPassword']"
        self.elements.first_name_input = "[data-testid='first-name'], #firstName, input[name='firstName']"
        self.elements.last_name_input = "[data-testid='last-name'], #lastName, input[name='lastName']"
        self.elements.phone_number_input = "[data-testid='phone-number'], #phoneNumber, input[type='tel'], input[name='phoneNumber']"
        self.elements.country_dropdown = "[data-testid='country'], #country, select[name='country']"
        self.elements.register_button = "[data-testid='register-button'], #registerBtn, button[type='submit'], button:has-text('Register')"
        self.elements.registration_form = "[data-testid='registration-form'], #registrationForm, form"

    def navigate_to_registration_page(self):
        """Navigate to the registration page URL."""
        self.page.goto("/register")
        self.page.wait_for_load_state("load")

    def enter_username(self, username: str):
        """Clear and enter username into the username field."""
        self.username_input.clear()
        self.username_input.fill(username)

    def enter_email(self, email: str):
        """Clear and enter email into the email field."""
        self.email_input.clear()
        self.email_input.fill(email)

    def enter_password(self, password: str):
        """Clear and enter password into the password field."""
        self.password_input.clear()
        self.password_input.fill(password)

    def enter_confirm_password(self, confirm_password: str):
        """Clear and enter password into the confirm password field."""
        self.confirm_password_input.clear()
        self.confirm_password_input.fill(confirm_password)

    def enter_first_name(self, first_name: str):
        """Clear and enter first name into the first name field."""
        self.first_name_input.clear()
        self.first_name_input.fill(first_name)

    def enter_last_name(self, last_name: str):
        """Clear and enter last name into the last name field."""
        self.last_name_input.clear()
        self.last_name_input.fill(last_name)

    def enter_phone_number(self, phone_number: str):
        """Clear and enter phone number into the phone number field."""
        self.phone_number_input.clear()
        self.phone_number_input.fill(phone_number)

    def select_country(self, country: str):
        """Click country dropdown and select the specified country."""
        self.country_dropdown.click()
        self.country_dropdown.select_option(label=country)

    def click_register_button(self):
        """Click the register button to submit the registration form."""
        self.register_button.click()

    def verify_registration_page_loaded(self):
        """Verify that the registration page has loaded by checking form visibility."""
        return self.registration_form.is_visible()

    def fill_registration_form(self, username: str, email: str, password: str, 
                               confirm_password: str, first_name: str, 
                               last_name: str, phone_number: str, country: str):
        """Fill all registration form fields with provided data."""
        self.enter_username(username)
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(confirm_password)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_phone_number(phone_number)
        self.select_country(country)
