from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I visit the veterinary animal editor page for "Test_vet"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/animal_editor/')


@then(u'There is a list with the "Test_animal" that the veterinary "Test_vet" created')
def step_impl(context):
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_animal')]")


@then(u'There is a list with the "Test_animal_2" that the veterinary "Test_vet" created')
def step_impl(context):
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Test_animal_2')]")