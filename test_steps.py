import allure
from selene import be
from selene.support import by
from selene import browser
from allure_commons.types import Severity


def test_github(browser_config):
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.feature("Repo issues")
    allure.dynamic.story("The #76 issue presence")
    allure.dynamic.link("https://github.com", name="GitHub website")

    with allure.step('GitHub main page open'):
        browser.open('https://github.com')

    with allure.step('repository "eroshenkoam/allure-example" search'):
        browser.element('.header-search-button').click()
        browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()

    with allure.step('open repository'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('"Issues" tab open'):
        browser.element('#issues-tab').click()

    with allure.step('search for #76 issue'):
        browser.element(by.partial_text('#76')).should(be.visible)
