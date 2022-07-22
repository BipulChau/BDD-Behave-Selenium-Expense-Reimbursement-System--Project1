from behave import *
from selenium import webdriver


@given(u'Employee is in the log in page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given Employee is in the log in page')


@when(u'Input correct username')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Input correct username')


@when(u'correct password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When correct password')


@then(u'redirect to logged in page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then redirect to logged in page')
