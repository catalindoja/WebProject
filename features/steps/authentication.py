from behave import *
import time
from django.contrib.auth import get_user_model
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)

    get_user_model().objects.create_user(username=username, password=password, email=username+"@gmail.com")
    context.selenium.get(f'{context.test.live_server_url}')

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    context.selenium.get(f'{context.test.live_server_url}')

    # Fill Login Information
    username_field= context.selenium.find_element_by_id("id_username")
    username_field.send_keys(username)
    password_field = context.selenium.find_element_by_id("id_password")
    password_field.send_keys(password)

    # Locate login button and click on it
    context.selenium.find_element_by_xpath('/html/body/form/center/div/table/tbody/tr[5]/td/input[2]').click()
    # Check we have logged in correctly
    assert context.selenium.find_element_by_xpath("//*[contains(text(), 'Welcome to our Zoo page')]")


@given(u'I log in as an admin')
def step_impl(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    context.selenium = webdriver.Chrome(options=chrome_options)
    # Login to the Admin Panel
    context.selenium.get(f'{context.test.live_server_url}/admin/')


    # Fill Login Information
    username = context.selenium.find_element_by_id("id_username")
    username.send_keys("admin")
    password = context.selenium.find_element_by_id("id_password")
    password.send_keys("admin")

    # Locate login button and click on it
    context.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
    context.test.assertEquals(context.selenium.title, "Site administration | Django site admin")