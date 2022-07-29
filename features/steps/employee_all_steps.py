from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given(u'Employee is logged in')
def step_impl(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("http://127.0.0.1:5501/index.html")
    correct_username = context.driver.find_element(By.XPATH, "//*[@id='username']")
    correct_username.send_keys('shaquera7')
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


@when(u'Checks all the functionalities')
def step_impl(context):
    # check reimbursement details and status
    check_reimbursement_details = context.driver.find_element(By.XPATH, "//button[@class='button is-success is-light']")
    check_reimbursement_details.click()
    time.sleep(2)
    select = Select(context.driver.find_element(By.XPATH, "//select[@id='status']"))
    # select by visible text
    select.select_by_value('pending')
    time.sleep(2)
    select.select_by_visible_text('approved')
    time.sleep(2)
    select.select_by_value('denied')
    time.sleep(2)

    # check create reimbursement
    create_reimbursement = context.driver.find_element(By.XPATH, "//a[text()='Create Reimbursement']")
    create_reimbursement.click()
    time.sleep(2)
    select_expense = Select(context.driver.find_element(By.XPATH, "//select[@id='typeOfExpense']"))
    select_expense.select_by_value("Food")
    time.sleep(1)
    reimbursement_amount = context.driver.find_element(By.XPATH, "//input[@id='reimbursementAmt']")
    reimbursement_amount.send_keys("35")
    time.sleep(2)
    description = context.driver.find_element(By.XPATH, "//textarea[@id='description']")
    description.send_keys("Lunch during Java Training")
    time.sleep(2)
    submit_btn = context.driver.find_element(By.XPATH, "//button[@id='expenseCreateBtn']")
    submit_btn.click()
    time.sleep(3)
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


@then(u'Should logout at the end')
def step_impl(context):
    logout_btn = context.driver.find_element(By.XPATH, "//a[@id='logout']")
    logout_btn.click()
    time.sleep(2)
    window_after = context.driver.window_handles[0]
    context.driver.switch_to.window(window_after)
    time.sleep(3)
    context.driver.quit()
