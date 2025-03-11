# Disclaimer: This output contains AI generated content, user is advised to review it before consumption.
# *Start of AI Generated Content*```
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('User is on the login page')
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('User enters valid credentials')
def enter_valid_credentials(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys("valid_username")
    password_input.send_keys("valid_password")

@when('User enters invalid credentials')
def enter_invalid_credentials(context):
    username_input = context.driver.find_element(By.ID, "user-name")
    password_input = context.driver.find_element(By.ID, "password")
    username_input.send_keys("invalid_username")
    password_input.send_keys("invalid_password")

@when('User clicks on the login button')
def click_login_button(context):
    login_button = context.driver.find_element(By.ID, "login-button")
    login_button.click()

@then('User should be redirected to the home page')
def verify_home_page_redirect(context):
    WebDriverWait(context.driver, 10).until(EC.url_contains("https://www.saucedemo.com/inventory.html"))

@then('Page title should contain "Swag Labs"')
def verify_page_title(context):
    assert "Swag Labs" in context.driver.title

@then('An error message starting with "Epic sadface" should be displayed')
def verify_error_message(context):
    error_message = context.driver.find_element(By.XPATH, "//h3[contains(text(),'Epic sadface')]")
    assert error_message.is_displayed()

# *End of AI Generated Content*