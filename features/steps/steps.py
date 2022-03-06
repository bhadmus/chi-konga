from time import sleep

from behave import *

from resources.page_objects import Konga
from element_mapper.element_mapper import *

use_step_matcher('parse')

@given(u'I am on konga site')
def step_impl(context):
    context.driver = Konga()
    context.driver.open_site()


@when(u'I click the login link')
def step_impl(context):
    context.driver.wait_to_be_clickable(Login.login_link)
    context.driver.click_any_element(Login.login_link)


@when(u'I fill in the username')
def step_impl(context):
    context.driver.wait_for_visibility(Login.email_field)
    context.driver.type_any_text(Login.email_field, Login.username1)


@when(u'I fill in the password')
def step_impl(context):
    context.driver.type_any_text(Login.password_field, Login.password1)


@when(u'I click the login button')
def step_impl(context):
    context.driver.click_any_element(Login.login_button)


@then(u'I should see the homepage')
def step_impl(context):
    sleep(5)
