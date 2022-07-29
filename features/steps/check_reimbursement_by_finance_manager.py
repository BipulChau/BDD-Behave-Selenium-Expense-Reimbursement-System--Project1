from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('Finance Manager is successfully logged-in and is inside the application')
def finance_manager_logged_in(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("http://127.0.0.1:5501/index.html")
    correct_username = context.driver.find_element(By.XPATH, "//*[@id='username']")
    correct_username.send_keys('bipul513')
    correct_password = context.driver.find_element(By.XPATH, "//*[@id='password']")
    correct_password.send_keys('password')
    login_button = context.driver.find_element(By.XPATH, "//*[@id='login']")
    login_button.click()
    window_after = context.driver.window_handles[0]
    context.driver.switch_to.window(window_after)
    time.sleep(1)


@when('Clicks Check Reimbursement Details')
def click_check_reimbursement_details(context):
    check_reimbursement_details = context.driver.find_element(By.XPATH, "//button[@class='button is-success is-light']")
    check_reimbursement_details.click()
    time.sleep(3)
    context.driver.quit()


@then(u'Should be able to see Reimbursement details of all the employees')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Should be able to see Reimbursement details of all the employees')
