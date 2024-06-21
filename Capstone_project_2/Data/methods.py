

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Capstone_project_2.Utilities.Utilities import LoginLocators as lc
from Capstone_project_2.Utilities import Utilities as vl



class TestMethods:

    @staticmethod
    def validation_on_admin_page(driver):
        admin_page = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.admin)))
        admin_page.click()
        xpaths = vl.xpath_admin_page
        headers_present = []
        header_not_present = []
        for i in xpaths:
            try:
                y = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,i)))
                header = y.text
                headers_present.append(header)
            except TimeoutException:
                pass
            else:
                header_not_present.append(i)
        return headers_present


    @staticmethod
    def title_verification(driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.title)))
            result = "OrangeHRM"
            return result
        except TimeoutException:
            result = "Title not found"
            return result

    @staticmethod
    def login_to_OragneHRM_stat(driver,username,password):
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element)))
        password_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element)))
        submit_button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("dashboard"))
            result = "The user has logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result

    @staticmethod
    def validate_main_menu(driver):
        xpaths = vl.xpaths_main_menu
        menu_present = []
        menu_not_present = []
        for i in xpaths:
            try:
                y = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, i)))
                header = y.text
                menu_present.append(header)
            except TimeoutException:
                pass
            else:
                menu_not_present.append(i)
        return menu_present

    @staticmethod
    def forgot_password_link(driver):
        driver.get(vl.login_url)
        forgot_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.forgot_password)))
        forgot_password.click()
        username_textbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_text_box)))
        username_textbox.send_keys(lc.valid_username)
        reset_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.reset_password)))
        reset_password.click()
        try:
            reset_password_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.header_6)))
            value = reset_password_element.text
            result = value
            return result
        except TimeoutError:
            result = "Invalid username"
            return result