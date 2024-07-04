import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Capstone.Pages.login import LoginMethods as LM
from Capstone.Pages.home import HomeMethods as HM
from Capstone.Locators import locators as lc
from Capstone.Locators.locators import LoginLocators as LL



@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope='session')
def class_inst(driver):
    logins = LM(driver)
    return logins

@pytest.fixture(scope='session')
def clas_inst(driver):
    logs = HM(driver)
    return logs


def test_TC_Login_01(class_inst):
    url = lc.login_url
    class_inst.go_to_page(url)
    result = class_inst.login_to_OragneHRM(LL.valid_username,LL.valid_password)
    assert result == 'The user is logged in successfully'

def test_TC_Login_02(class_inst):
    result = class_inst.login_to_OragneHRM(LL.invalid_username,LL.invalid_password)
    assert result == 'Invalid credentials'

def test_TC_PIM_01(clas_inst):
    url = lc.login_url
    clas_inst.go_to_page(url)
    clas_inst.login_to_OragneHRM_stat(LL.valid_username,LL.valid_password)
    name = clas_inst.random_name()
    result = clas_inst.add_new_employee(name[0],name[1])
    assert result == 'Successfully Saved'

def test_TC_PIM_02(clas_inst):
    result = clas_inst.edit_employee_details()
    assert result == 'Successfully Updated'

def test_TC_PIM_03(clas_inst):
    result = clas_inst.delete_employee()
    assert result == 'Successfully Deleted'









