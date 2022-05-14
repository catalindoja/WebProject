from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@given(u'I register a zoo "Zoo Barcelona"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/create_zoo')
    name_field = context.selenium.find_element_by_name("name")
    name_field.send_keys("Zoo Barcelona")
    description_field = context.selenium.find_element_by_id("id_description")
    description_field.send_keys("Zoo de la ciutat de Barcelona")
    max_vistors_field = context.selenium.find_element_by_id("id_max_visitors")
    max_vistors_field.send_keys("100")
    address_field = context.selenium.find_element_by_id("id_address")
    address_field.send_keys("Plaça Catalunya")
    postal_code_field = context.selenium.find_element_by_id("id_postalcode")
    postal_code_field.send_keys("25000")
    # Click submit button
    context.selenium.find_element_by_xpath('/html/body/center/div/form/table/tbody/tr[6]/td/input').click() #TODO: Fix xpath


@then(u'I\'m viewing the admin page')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/zoo/') #TODO: Check url
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("admin")
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys("admin")
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


@then(u'There is 1 zoo called "Zoo Barcelona"')
def step_impl(context):
    # Check there is one zoo
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 zoo')]")
    # Check it's called Zoo Barcelona
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Zoo Barcelona')]")