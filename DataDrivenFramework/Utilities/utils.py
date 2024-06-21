import xlrd
import xlwt
from xlutils.copy import copy
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import DataDrivenFramework.Data.login_data as variables
from DataDrivenFramework.Data.login_data import Login_locators


class Common():

    def __init__(self,driver):
        self.driver = driver
        self.index = 1

    def read_credentials(self,file_path, sheet_name):
        workbook = xlrd.open_workbook(file_path)
        sheet = workbook.sheet_by_name(sheet_name)
        creds = []
        for i in range(1, sheet.nrows):
            index_value = i
            username = sheet.cell_value(i, 1)
            password = sheet.cell_value(i, 2)
            creds.append((index_value,username, password))
        return creds


    def login(self,username,password):
        self.driver.get(variables.login_url)
        username_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Login_locators.username_element)))
        password_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Login_locators.password_element)))
        submit_button_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Login_locators.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(self.driver, 10).until(
                EC.url_matches(variables.home_url))
            profile_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Login_locators.profile_button_element)))
            profile_button.click()
            logout_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, Login_locators.logout_button_element)))
            logout_button.click()
            return print("The user has logged in successfully")
        except TimeoutException:
            return print("Invalid credentials")


    def fill_the_sheet(self,file_path,index,status):
        workbook = xlrd.open_workbook(file_path)
        wr = copy(workbook)
        if status == "passed":
            wr.get_sheet(0).write(index, 6, "Passed")
            wr.save(file_path)
        else:
            wr.get_sheet(0).write(index, 6, "Failed")
            wr.save(file_path)







