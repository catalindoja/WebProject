from behave import *

use_step_matcher("parse")

@given('Exists a user "{username}" with password "{password}"')
def step_impl(context, username, password):
    from django.contrib.auth import get_user_model
    get_user_model().objects.create_user(username=username, password=password)

@given('I login as user "{username}" with password "{password}"')
def step_impl(context, username, password):
    context.browser.visit(context.get_url(''))
    form = context.browser.find_by_tag('form').first
    context.browser.fill('username', username)
    context.browser.fill('password', password)
    form.find_by_value('Login').first.click()
    assert context.browser.is_text_present("Welcome to our Zoo page")

@given('I\'m not logged in')
def step_impl(context):
    context.browser.visit(context.get_url('logout')+'?next=/zooproject/')
    assert context.browser.is_text_present('login')
