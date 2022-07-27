from behave import *
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('Employee is in the log in page')
def open_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get("http://127.0.0.1:5501/index.html")
    time.sleep(1)


@when(u'Input correct username')
def input_username(context):
    input_correct_username = context.driver.find_element(By.XPATH, "//*[@id='username']")
    input_correct_username.send_keys('bipul513')
    time.sleep(3)
    context.driver.quit()


@when(u'correct password')
def input_correct_password(context):
    pass


@then(u'redirect to logged in page')
def step_impl(context):
    pass
