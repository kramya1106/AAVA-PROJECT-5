"""
Test Case ID: TC_REG_001
Title: Verify User Registration with Valid Data
Description: This test case verifies that a new user can successfully register on the application by providing valid registration details including username, email, password, and personal information. The test validates all input fields, form submission, and successful account creation.
"""

import traceback
import pytest
from core.playwright_manager import PlaywrightManager
from core.settings import framework_logger
from pages.registration_page import RegistrationPage
from pages.success_page import SuccessPage
from playwright.sync_api import expect
import test_flows_common.test_flows_common as common
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@pytest.mark.usefixtures("main_execution")
def test_tc_reg_001_user_registration(stage_callback, tc_tracer, reporter):
    tcid = "TC_REG_001"
    current_step = "Step 0"
    current_validation = "Initialization"

    try:
        common.setup()

        # ── Precondition: Navigate to registration page ──
        current_step = "Precondition"
        current_validation = "User should be on the registration page"

        with PlaywrightManager() as page:
            registration_page = RegistrationPage(page)
            registration_page.navigate_to_registration_page()
            expect(registration_page.registration_form).to_be_visible(timeout=30000)
            stage_callback("precondition_registration_page", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Precondition: Navigated to registration page")
            reporter.validate(True, f"[{tcid}] Precondition: Navigated to registration page")

            # ── Step 1: Enter valid username in the Username field ──
            current_step = "Step 1"
            current_validation = "Username should be accepted and displayed in the field"

            expect(registration_page.username_input).to_be_visible(timeout=30000)
            expect(registration_page.username_input).to_be_enabled(timeout=5000)
            registration_page.username_input.clear()
            registration_page.username_input.fill("testuser123")
            expect(registration_page.username_input).to_have_value("testuser123", timeout=5000)
            stage_callback("step1_username_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 1: Username 'testuser123' entered and verified")
            reporter.validate(True, f"[{tcid}] Step 1: Username 'testuser123' entered and verified")

            # ── Step 2: Enter valid email address in the Email field ──
            current_step = "Step 2"
            current_validation = "Email should be accepted and displayed in the field"

            expect(registration_page.email_input).to_be_visible(timeout=30000)
            expect(registration_page.email_input).to_be_enabled(timeout=5000)
            registration_page.email_input.clear()
            registration_page.email_input.fill("testuser@example.com")
            expect(registration_page.email_input).to_have_value("testuser@example.com", timeout=5000)
            stage_callback("step2_email_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 2: Email 'testuser@example.com' entered and verified")
            reporter.validate(True, f"[{tcid}] Step 2: Email 'testuser@example.com' entered and verified")

            # ── Step 3: Enter valid password in the Password field ──
            current_step = "Step 3"
            current_validation = "Password should be accepted and masked in the field"

            expect(registration_page.password_input).to_be_visible(timeout=30000)
            expect(registration_page.password_input).to_be_enabled(timeout=5000)
            registration_page.password_input.clear()
            registration_page.password_input.fill("Test@1234")
            password_type = registration_page.password_input.get_attribute("type")
            reporter.validate(
                password_type == "password",
                f"[{tcid}] Step 3: Password field type is 'password' (masked)"
            )
            stage_callback("step3_password_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 3: Password entered and verified as masked")
            reporter.validate(True, f"[{tcid}] Step 3: Password entered and verified as masked")

            # ── Step 4: Re-enter the same password in the Confirm Password field ──
            current_step = "Step 4"
            current_validation = "Confirm Password should be accepted and masked in the field"

            expect(registration_page.confirm_password_input).to_be_visible(timeout=30000)
            expect(registration_page.confirm_password_input).to_be_enabled(timeout=5000)
            registration_page.confirm_password_input.clear()
            registration_page.confirm_password_input.fill("Test@1234")
            confirm_password_type = registration_page.confirm_password_input.get_attribute("type")
            reporter.validate(
                confirm_password_type == "password",
                f"[{tcid}] Step 4: Confirm password field type is 'password' (masked)"
            )
            stage_callback("step4_confirm_password_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 4: Confirm password entered and verified as masked")
            reporter.validate(True, f"[{tcid}] Step 4: Confirm password entered and verified as masked")

            # ── Step 5: Enter valid first name in the First Name field ──
            current_step = "Step 5"
            current_validation = "First Name should be accepted and displayed in the field"

            expect(registration_page.first_name_input).to_be_visible(timeout=30000)
            registration_page.first_name_input.clear()
            registration_page.first_name_input.fill("John")
            expect(registration_page.first_name_input).to_have_value("John", timeout=5000)
            stage_callback("step5_first_name_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 5: First name 'John' entered and verified")
            reporter.validate(True, f"[{tcid}] Step 5: First name 'John' entered and verified")

            # ── Step 6: Enter valid last name in the Last Name field ──
            current_step = "Step 6"
            current_validation = "Last Name should be accepted and displayed in the field"

            expect(registration_page.last_name_input).to_be_visible(timeout=30000)
            registration_page.last_name_input.clear()
            registration_page.last_name_input.fill("Doe")
            expect(registration_page.last_name_input).to_have_value("Doe", timeout=5000)
            stage_callback("step6_last_name_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 6: Last name 'Doe' entered and verified")
            reporter.validate(True, f"[{tcid}] Step 6: Last name 'Doe' entered and verified")

            # ── Step 7: Enter valid phone number in the Phone Number field ──
            current_step = "Step 7"
            current_validation = "Phone Number should be accepted and displayed in the field"

            expect(registration_page.phone_number_input).to_be_visible(timeout=30000)
            registration_page.phone_number_input.clear()
            registration_page.phone_number_input.fill("1234567890")
            expect(registration_page.phone_number_input).to_have_value("1234567890", timeout=5000)
            stage_callback("step7_phone_number_entered", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 7: Phone number '1234567890' entered and verified")
            reporter.validate(True, f"[{tcid}] Step 7: Phone number '1234567890' entered and verified")

            # ── Step 8: Select a country from the Country dropdown ──
            current_step = "Step 8"
            current_validation = "Selected country should be displayed in the dropdown"

            expect(registration_page.country_dropdown).to_be_visible(timeout=30000)
            expect(registration_page.country_dropdown).to_be_enabled(timeout=5000)
            registration_page.country_dropdown.click()
            page.wait_for_load_state("domcontentloaded", timeout=5000)
            registration_page.country_dropdown.select_option(label="United States")
            selected_value = registration_page.country_dropdown.input_value()
            reporter.validate(
                "United States" in selected_value or selected_value == "United States",
                f"[{tcid}] Step 8: Country 'United States' selected in dropdown"
            )
            stage_callback("step8_country_selected", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 8: Country 'United States' selected and verified")
            reporter.validate(True, f"[{tcid}] Step 8: Country 'United States' selected and verified")

            # ── Step 9: Click on the Register button ──
            current_step = "Step 9"
            current_validation = "Registration should be processed and user should be redirected to success page"

            expect(registration_page.register_button).to_be_visible(timeout=30000)
            expect(registration_page.register_button).to_be_enabled(timeout=10000)
            registration_page.register_button.click()
            page.wait_for_load_state("networkidle", timeout=60000)
            stage_callback("step9_register_button_clicked", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 9: Register button clicked and form submitted")
            reporter.validate(True, f"[{tcid}] Step 9: Register button clicked and form submitted")

            # ── Step 10: Verify success message is displayed ──
            current_step = "Step 10"
            current_validation = "Success message 'Registration Successful' should be displayed"

            success_page = SuccessPage(page)
            expect(success_page.success_message).to_be_visible(timeout=30000)
            success_message_text = success_page.success_message.text_content()
            reporter.validate(
                "Registration Successful" in success_message_text,
                f"[{tcid}] Step 10: Success message contains 'Registration Successful'"
            )
            stage_callback("step10_success_message_verified", page, screenshot_only=True)
            framework_logger.info(f"[{tcid}] Step 10: Success message 'Registration Successful' verified")
            reporter.validate(True, f"[{tcid}] Step 10: Success message 'Registration Successful' verified")

    except Exception as e:
        framework_logger.error(
            f"[{tcid}] Test failed at {current_step} — {current_validation}: "
            f"{e}\n{traceback.format_exc()}"
        )
        reporter.validate(False, f"[{tcid}] FAIL at {current_step} — {current_validation}: {str(e)}")
        raise
