# Disclaimer: This output contains AI generated content, user is advised to review it before consumption.
# *Start of AI Generated Content*```
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then

@given('User is on the login page')
def open_login_page(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")

@when('User enters valid username and password')
def enter_valid_credentials(context):
    username_input = context.driver.find_element(By.ID, 'user-name')
    username_input.send_keys('valid_username')
    password_input = context.driver.find_element(By.ID, 'password')
    password_input.send_keys('valid_password')

@when('User enters invalid username and password')
def enter_invalid_credentials(context):
    username_input = context.driver.find_element(By.ID, 'user-name')
    username_input.send_keys('invalid_username')
    password_input = context.driver.find_element(By.ID, 'password')
    password_input.send_keys('invalid_password')

@when('User clicks on the login button')
def click_login_button(context):
    login_button = context.driver.find_element(By.ID, 'login-button')
    login_button.click()

@then('User should be redirected to the home page')
def verify_redirect_to_home_page(context):
    assert "https://www.saucedemo.com/inventory.html" in context.driver.current_url

@then('Page title should contain "Swag Labs"')
def verify_page_title(context):
    assert "Swag Labs" in context.driver.title

@then('Error message should start with "Epic sadface"')
def verify_error_message(context):
    error_message = context.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="error"]')
    assert error_message.text.startswith("Epic sadface")

# *End of AI Generated Content*