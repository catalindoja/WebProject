from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I register a visitor "Test_visitor" assigned to "Zoo Barcelona"')
def step_impl(context):
    # Login to the Admin Panel
    context.selenium.get(f'{context.test.live_server_url}/registration/register_visitor')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("Test_visitor")
    password1_field = context.selenium.find_element_by_id("id_password1")
    password1_field.send_keys("prova1234@")

    password2_field = context.selenium.find_element_by_id("id_password2")
    password2_field.send_keys("prova1234@")
    name_field = context.selenium.find_element_by_id("id_name")
    name_field.send_keys("Test_visitor")
    telephone_field = context.selenium.find_element_by_id("id_telephone")
    telephone_field.send_keys("973973973")
    email_field = context.selenium.find_element_by_id("id_email")
    email_field.send_keys("Test_visitor@email.com")
    age_field = context.selenium.find_element_by_id("id_age")
    age_field.send_keys("25")
    zoo_id_field = Select(context.selenium.find_element_by_id('id_zoo_id'))
    zoo_id_field.select_by_visible_text("Zoo Barcelona")
    context.selenium.find_element_by_xpath('/html/body/div[2]/form/input[2]').click()


@then(u'I\'m viewing the admin page for the visitors')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/admin/zooproject/visitor/')
    username_field = context.selenium.find_element_by_id("id_username")
    username_field.send_keys("admin")
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys("admin")
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

@then(u'There is 1 visitor called "Test_visitor"')
def step_impl(context):
    # Check there is one zoo
    assert context.selenium.find_element_by_xpath("//*[contains(text(), '1 visitor')]")
    # Check it's called Zoo Barcelona
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_visitor')]")
