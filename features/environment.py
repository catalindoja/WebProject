import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SampleDemo.settings')
django.setup()

from behave import fixture, use_fixture
from django.contrib.auth import get_user_model
from django.test.runner import DiscoverRunner
from django.test.testcases import LiveServerTestCase


class BaseTestCase(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        get_user_model().objects.create_superuser(username='admin', password='admin', email='admin@admin.com')
        super(BaseTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        get_user_model().objects.filter().delete()
        super(BaseTestCase, cls).tearDownClass()


@fixture
def django_test_case(context):
    context.test_case = BaseTestCase
    context.test_case.setUpClass()
    yield
    context.test_case.tearDownClass()
    context.selenium.quit()
    del context.test_case


def before_all(context):
    django.setup()
    context.test_runner = DiscoverRunner()
    context.test_runner.setup_test_environment()
    context.old_db_config = context.test_runner.setup_databases()
    yield
    context.test_runner.teardown_databases(context.old_db_config)
    context.test_runner.teardown_test_environment()


def before_scenario(context, scenario):
    use_fixture(django_test_case, context)