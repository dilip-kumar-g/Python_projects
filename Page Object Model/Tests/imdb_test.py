import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import IMDB.Locators.locators as values
from IMDB.Pages.adv_search import Advanced_search as d
from IMDB.Locators.locators import Finds



@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def search_inst(driver):
    search = d(driver)
    return search


def test_name_page(search_inst):
    url = Finds.name_search_url
    page = search_inst.go_to_page(url)
    assert page == True


def test_enter_name(search_inst):
    name = Finds.name_module
    open_name_module = search_inst.handling_modules(name)
    name_element = Finds.name_input_element
    ele = search_inst.non_clickable_elements(name_element)
    ele.send_keys(values.search_name)
    assert open_name_module == True


def test_enter_birthdate(search_inst):
    date = Finds.date_module
    open_date_module = search_inst.handling_modules(date)
    start_date_element = Finds.start_date_element
    ele = search_inst.non_clickable_elements(start_date_element)
    ele.send_keys(values.start_date)
    end_date_element = Finds.end_date_element
    elem = search_inst.non_clickable_elements(end_date_element)
    elem.send_keys(values.start_date)
    assert open_date_module == True


def test_check_results_of_search(search_inst):
    check_result = search_inst.check_result(values.see_result_button,values.results)
    assert check_result == True
