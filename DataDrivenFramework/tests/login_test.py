import pytest
from selenium import webdriver
from DataDrivenFramework.Utilities.utils import Common
import DataDrivenFramework.Data.login_data as variables

# Fixture to initialize WebDriver
@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def class_inst(driver):
    com = Common(driver)
    return com


def test_data_extract(class_inst):
    values = class_inst.read_credentials(variables.file_path,"usercreds")
    assert values is not None, "No data in the sheet"
    return values


# Define test_login function to test login with extracted data
def test_login(class_inst):
    extracted_values = class_inst.read_credentials(variables.file_path,"usercreds")
    for index, username, password in extracted_values:
        result = class_inst.login(username, password)
        if result == "The user has logged in successfully":
            class_inst.fill_the_sheet(variables.file_path, index, status="Passed")
        else:
            class_inst.fill_the_sheet(variables.file_path, index, status="Failed")

