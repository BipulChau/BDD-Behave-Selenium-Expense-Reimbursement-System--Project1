from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('Finance Manager has successfully logged in and clicked check reimbursement details')
def finance_manager_logged_in_and_clicked_check_reimbursement_details(context):
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
    time.sleep(2)
    check_reimbursement_details = context.driver.find_element(By.XPATH, "//button[@class='button is-success is-light']")
    check_reimbursement_details.click()
    time.sleep(3)


@when(u'select status as pending, approved and denied')
def step_impl(context):
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
    # select by visible text
    select.select_by_value('pending')
    time.sleep(2)
    select.select_by_visible_text('approved')
    time.sleep(2)
    # select by value
    select.select_by_value('denied')
    time.sleep(2)


@then('Reimbursements should filter as pending, approved and denied')
def step_impl(context):
    context.driver.quit()
