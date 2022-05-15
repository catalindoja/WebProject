from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I register a veterinary "Test_staff" assigned to "Zoo Barcelona"')
def step_impl(context):
    # Login to the Admin Panel
    context.selenium.get(f'{context.test.live_server_url}/registration/register_staff')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("Test_staff")
    password1_field = context.selenium.find_element_by_id("id_password1")
    password1_field.send_keys("prova1234@")

    password2_field = context.selenium.find_element_by_id("id_password2")
    password2_field.send_keys("prova1234@")
    name_field = context.selenium.find_element_by_id("id_name")
    name_field.send_keys("Test_staff")
    age_field = context.selenium.find_element_by_id("id_age")
    age_field.send_keys(25)
    address_field = context.selenium.find_element_by_id("id_address")
    address_field.send_keys("Carrer prova")
    postal_code_field = context.selenium.find_element_by_id("id_postalcode")
    postal_code_field.send_keys("25000")
    
    zoo_id_field = Select(context.selenium.find_element_by_id('id_zoo_id'))
    zoo_id_field.select_by_visible_text("Zoo Barcelona")
    
    assigned_habitat_field = context.selenium.find_element_by_id("id_assigned_habitat")
    assigned_habitat_field.send_keys("Piscina Dofins")

    context.selenium.find_element_by_xpath('/html/body/div[2]/form/input[2]').click()


@then(u'I\'m viewing the admin page for the staffs')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/staff/')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("admin")
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys("admin")
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()


@then(u'There is 1 staff called "Test_staff"')
def step_impl(context):
    # Check there is one veterinary
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 staff')]")
    # Check he's called Test_vet
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_staff')]")

