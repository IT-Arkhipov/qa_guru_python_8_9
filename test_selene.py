from selene import be
from selene.support import by
from selene import browser


def test_github(browser_config):
    browser.open('https://github.com')
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys('eroshenkoam/allure-example').submit()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()
    browser.element(by.partial_text('#76')).should(be.visible)
