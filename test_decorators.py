import allure
from allure_commons.types import Severity
from selene import be
from selene.support import by
from selene import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "arkhipovab")
@allure.feature("Repo issues")
@allure.story("The #76 issue presence")
@allure.link("https://github.com", name="GitHub website")
def test_github(browser_config):
    open_main_page()
    repo_search('eroshenkoam/allure-example')
    open_repo('eroshenkoam/allure-example')
    issues_tab_open()
    search_for_text('#76')


@allure.step('GitHub main page open')
def open_main_page():
    browser.open('https://github.com')


@allure.step('repository {repo} search')
def repo_search(repo):
    browser.element('.header-search-button').click()
    browser.element('#query-builder-test').send_keys(repo).submit()


@allure.step('open repository {repo}')
def open_repo(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('"Issues" tab open')
def issues_tab_open():
    browser.element('#issues-tab').click()


@allure.step('search for {text} issue')
def search_for_text(text):
    browser.element(by.partial_text(text)).should(be.visible)
