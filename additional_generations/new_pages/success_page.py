"""
Page object for success/confirmation page.
This page object represents the success page displayed after successful user registration.
"""

from playwright.sync_api import Page
from pages.base_page_object import BasePageObject


class SuccessPage(BasePageObject):
    """Page object for the success/confirmation page after registration."""

    def __init__(self, page: Page):
        super().__init__(page)
        self.elements.success_message = "[data-testid='success-message'], .success-message, #successMsg, .alert-success"
        self.elements.success_page_indicator = "[data-testid='success-page'], .success-container, #successPage"

    def get_success_message_text(self):
        """Retrieve the text content of the success message element."""
        return self.success_message.text_content()

    def verify_success_message_visible(self):
        """Verify that the success message is visible on the page."""
        return self.success_message.is_visible()

    def verify_success_page_loaded(self):
        """Verify that the success page has loaded successfully."""
        return self.success_page_indicator.is_visible()
