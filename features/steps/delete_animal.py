from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")


@when(u'I delete the animal "Test_animal"')
def step_impl(context):
    context.selenium.get(f'{context.test.live_server_url}/animal_delete/1/')
    context.selenium.find_element_by_xpath('/html/body/div/form/input[2]').click()


