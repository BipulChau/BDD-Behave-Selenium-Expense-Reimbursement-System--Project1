from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('The finance manager is logged in, clicked Check Reimbursement Details and filter status as pending')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("http://127.0.0.1:5501/index.html")
    correct_username = context.driver.find_element(By.XPATH, "//*[@id='username']")
    correct_username.send_keys('bipul513')
    time.sleep(3)
    correct_password = context.driver.find_element(By.XPATH, "//*[@id='password']")
    correct_password.send_keys('password')
    time.sleep(1)
    login_button = context.driver.find_element(By.XPATH, "//*[@id='login']")
    login_button.click()
    time.sleep(1)
    window_after = context.driver.window_handles[0]
    context.driver.switch_to.window(window_after)
    time.sleep(2)
    check_reimbursement_details = context.driver.find_element(By.XPATH, "//button[@class='button is-success is-light']")
    check_reimbursement_details.click()
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
    # select by visible text
    select.select_by_value('pending')
    time.sleep(2)


@when('clicks approve')
def step_impl(context):
    approve_btn = context.driver.find_element(By.XPATH, "//button[@id='status-approve']")
    approve_btn.click()
    time.sleep(2)


@when('clicks deny')
def step_impl(context):
    home = context.driver.find_element(By.XPATH, "//*[@href='loggedin.html']")
    home.click()
    time.sleep(2)
    check_reimbursement_details = context.driver.find_element(By.XPATH, "//button[@class='button is-success is-light']")
    check_reimbursement_details.click()
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
    # select by visible text
    time.sleep(2)
    select.select_by_value('pending')
    time.sleep(2)
    deny_btn = context.driver.find_element(By.XPATH, "//button[@class='button is-danger is-active']")
    deny_btn.click()
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
    select.select_by_visible_text('approved')
    time.sleep(2)
    select.select_by_value('pending')
    time.sleep(2)
    select.select_by_value('denied')


@then('That particular reimbursement should disappear from pending status')
def step_impl(context):
    time.sleep(2)


@then(u'logout')
def step_impl(context):
    logout_btn = context.driver.find_element(By.XPATH, "//a[@id='logout']")
    logout_btn.click()
    time.sleep(2)
    window_after = context.driver.window_handles[0]
    context.driver.switch_to.window(window_after)
    time.sleep(3)
    context.driver.quit()
