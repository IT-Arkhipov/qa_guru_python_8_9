from selene import browser
import pytest
from init import settings
import allure
from allure_commons.types import AttachmentType


def pytest_addoption(parser):
    parser.addoption('--password', default='not set')


@pytest.fixture
def browser_config(request):
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    settings.password = request.config.getoption('--password')

    yield

    allure.attach(settings.password, 'password', AttachmentType.TEXT, '.txt')
    browser.quit()
