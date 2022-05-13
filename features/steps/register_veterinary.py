from behave import *
from functools import reduce
from django.db.models import Q
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


use_step_matcher("re")

@given(u'I am on the Django Admin')
def step_impl(context):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    # Login to the Admin Panel
    context.selenium.get(f'http://127.0.0.1:8000/admin/')

    # Fill Login Information
    username = context.selenium.find_element_by_id("id_username")
    username.send_keys("admin")
    password = context.selenium.find_element_by_id("id_password")
    password.send_keys("admin")

    # Locate login button and click on it
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
    context.test.assertEquals(context.selenium.title, "Site administration | Django site admin")

@when(u'I register veterinary')
def step_impl(context):
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    # Login to the Admin Panel
    context.selenium.get(f'http://127.0.0.1:8000/registration/register_veterinary')
    username = context.selenium.find_element_by_id("id_username")
    username.send_keys("Test_guy")
    password1 = context.selenium.find_element_by_id("id_password1")
    password1.send_keys("prova1234@")
    password2 = context.selenium.find_element_by_id("id_password2")
    password2.send_keys("prova1234@")

    name = context.selenium.find_element_by_id("id_name")
    name.send_keys("Test_guy")
    age = context.selenium.find_element_by_id("id_age")
    age.send_keys(25)
    address = context.selenium.find_element_by_id("id_address")
    address.send_keys("Carrer prova")
    postalCode = context.selenium.find_element_by_id("id_postalcode")
    postalCode.send_keys("25000")
    
    zooId = Select(context.selenium.find_element_by_id('id_zoo_id'))
    zooId.select_by_visible_text("Zoo 1")
    
    nAssignedAnimals = context.selenium.find_element_by_id("id_number_assigned_animals")
    nAssignedAnimals.send_keys("20")

    context.selenium.find_element_by_xpath('/html/body/div/form/input[2]').click()


@then(u'I\'m viewing the admin page')
def step_impl(context):
    print("hola")

@then(u'There are 1 veterinaries')
def step_impl(context):
    print("hola")
