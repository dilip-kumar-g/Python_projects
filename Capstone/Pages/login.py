import pdb

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Capstone.Locators.locators import LoginLocators as lc


class LoginMethods:

    def __init__(self,driver):
        self.driver = driver

    def go_to_page(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False


    def login_to_OragneHRM(self,username,password):
        username_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element)))
        password_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element)))
        submit_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_contains("dashboard"))
            profile_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.profile_button_element)))
            profile_button.click()
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.logout_button_element)))
            logout_button.click()
            result = "The user is logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result






























