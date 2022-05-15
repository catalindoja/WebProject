from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I edit the animal "Test_animal" to rename it to "Test_edited_animal"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/animal_editor/2')
    name_field = context.selenium.find_element_by_id("id_name")
    name_field.clear()
    name_field.send_keys("Test_edited_animal")
    context.selenium.find_element_by_xpath('/html/body/div/form/input[2]').click()


@then(u'There is 1 animal "Test_edited_animal"')
def step_impl(context):
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_edited_animal')]")


@then(u'There\'s no animal "Test_animal"')
def step_impl(context):
    body_text = context.selenium.find_element_by_tag_name("body").text
    assert 'Test_animal' not in body_text