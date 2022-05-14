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


@then(u'Exists a zoo "Zoo Barcelona"')
def step_impl(context):
    # Check in the admin page that the zoo has been created successfully
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/zoo')
    # Check if the created zoo exists by looking for its name in the page text
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Zoo Barcelona')]")


@when(u'I register a visitor "Test_guy" assigned to "Zoo Barcelona"')
def step_impl(context):
    # Login to the Admin Panel
    context.selenium.get(f'{context.test.live_server_url}/registration/register_visitor')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("Test_guy")
    password1_field = context.selenium.find_element_by_id("id_password1")
    password1_field.send_keys("prova1234@")

    password2_field = context.selenium.find_element_by_id("id_password2")
    password2_field.send_keys("prova1234@")
    name_field = context.selenium.find_element_by_id("id_name")
    name_field.send_keys("Test_guy")
    telephone_field = context.selenium.find_element_by_id("id_telephone")
    telephone_field.send_keys(973973973)
    email_field = context.selenium.find_element_by_id("id_email")
    email_field.send_keys(email@email.com)
    age_field = context.selenium.find_element_by_id("id_age")
    age_field.send_keys(25)
    date_last_visit_field = context.selenium.find_element_by_id("id_datelastvisit") #TODO: Check
    date_last_visit_field.send_keys("2022-05-14")
    zoo_id_field = context.selenium.find_element_by_id("id_zoo_id")
    zoo_id_field.select_by_visible_text("Zoo Barcelona")

    context.selenium.find_element_by_xpath('/html/body/div/form/input[2]').click() #TODO: Check xpath


@then(u'I\'m viewing the admin page')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/zoo/') #TODO: Check url. /zoo or /zoos?
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("admin")
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys("admin")
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


@then(u'There is 1 visitor called "Test_guy"')
def step_impl(context):
    # Check there is one zoo
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 visitor')]")
    # Check it's called Zoo Barcelona
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_guy')]")