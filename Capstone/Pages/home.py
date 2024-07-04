

from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Capstone.Locators.locators import LoginLocators as lc




class HomeMethods():

    def __init__(self,driver):
        self.driver = driver


    def go_to_page(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False

    def random_name(self):
        fake = Faker()
        f_n = fake.first_name()
        l_n = fake.last_name()
        return f_n,l_n


    def add_new_employee(self,first,last):
        pim_module = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.pim)))
        pim_module.click()
        add_employee = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.add_employee)))
        add_employee.click()
        first_name = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.fir_nam)))
        last_name = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.las_nam)))
        first_name.send_keys(first)
        last_name.send_keys(last)
        save_button = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.save)))
        save_button.click()
        try:
            toaster = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,lc.saved_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to save"
            return value


    def delete_employee(self):
        pim_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()
        employee_list = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.employee_list)))
        employee_list.click()
        select_user_del = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.sel_user_del)))
        select_user_del.click()
        delete_user = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.delete_user)))
        delete_user.click()
        confirm_delete = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.confirm_del)))
        confirm_delete.click()
        try:
            toaster = WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,lc.del_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to delete the selected user"
            return value


    def edit_employee_details(self):
        pim_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()
        employee_list = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.employee_list)))
        employee_list.click()
        select_user = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.sel_user_edit)))
        select_user.click()
        edit_user = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.click_edit)))
        edit_user.click()
        male_button = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.male_button)))
        male_button.click()
        submit_edited_user = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,lc.submit_edit_user)))
        submit_edited_user.click()
        try:
            toaster = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH,lc.update_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to update user details"
            return value


    def login_to_OragneHRM_stat(self, username, password):
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
            result = "The user has logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result