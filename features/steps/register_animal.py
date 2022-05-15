from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I create an animal "Test_animal" assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/create_animal')
    name_field = context.selenium.find_element_by_id("id_name")
    name_field.send_keys("Test_animal")
    
    zoo_id_field = Select(context.selenium.find_element_by_id('id_zoo_id'))
    zoo_id_field.select_by_visible_text("Zoo Barcelona")
    staff_id_field = Select(context.selenium.find_element_by_id('id_staff_id'))
    staff_id_field.select_by_visible_text("Test_staff")

    context.selenium.find_element_by_xpath('/html/body/div[2]/form/input[2]').click()


@then(u'I\'m viewing the admin page for the animals')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/animal/')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("admin")
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys("admin")
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


@then(u'There is 1 animal called "Test_animal"')
def step_impl(context):
    # Check there is one animal
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 animal')]")
    # Check he's called Test_animal
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_animal')]")


@when(u'I create an animal using the api assigned to the zoo "Zoo Barcelona", the veterinary "Test_vet" and the staff "Test_staff"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/create_animal')
    # Click autocomplete with api button
    context.selenium.find_element_by_xpath('/html/body/div[2]/form/button').click()
    time.sleep(1) # To have enough time to get the api response before submitting the form
    
    zoo_id_field = Select(context.selenium.find_element_by_id('id_zoo_id'))
    zoo_id_field.select_by_visible_text("Zoo Barcelona")
    staff_id_field = Select(context.selenium.find_element_by_id('id_staff_id'))
    staff_id_field.select_by_visible_text("Test_staff")

    # Click submit button
    context.selenium.find_element_by_xpath('/html/body/div[2]/form/input[2]').click()


@then(u'There is 1 animal')
def step_impl(context):
    # Check there is one animal
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 animal')]")


@when(u'I try to access the create animal page')
def step_impl(context):
    # Check there is one animal
    context.selenium.get(f'{context.test.live_server_url}/create_animal')


@then(u'I get redirected to log in as a veterinary')
def step_impl(context):
    assert context.selenium.find_element_by_id("id_username")
    time.sleep(10)