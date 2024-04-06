from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class cookies():

    def __init__ (self,url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com/")

    def get_cookies(self):
        cookies = self.driver.get_cookies()
        return cookies

    def login(self,username_value,password_value):
        username_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='user-name']"))
        )
        password_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        login_button = self.driver.find_element(By.XPATH, "//input[@id='login-button']")
        username_element.send_keys(username_value)
        password_element.send_keys(password_value)
        login_button.click()
        latest_cookies = self.driver.get_cookies()
        return latest_cookies

    def cookie_creation(self,latest_cookies):
        if cookies != latest_cookies:
            print("The cookies has been generated")
        else:
            print("The cookies has not been generated")

    def quit(self):
        self.driver.quit()


if __name__ == '__main__':
    url = "https://www.saucedemo.com/"
    cookie = cookies(url)
    print("Cookies before logging into sauce demo is",cookie.get_cookies())
    logged_in_cookies = cookie.login("standard_user","secret_sauce")
    print("Cookies after logging into sauce demo is \n", logged_in_cookies)
    cookie.cookie_creation(logged_in_cookies)
    cookie.quit()

"""
Using python selenium oops concepts i created a class name Cookies for the task, where i initiated the constructor and looged into the given url, i have a method to fetch cookies whenever i call it
and another method to login and fetch the cookies and printing the same in the console. There after verifying the same with another method if the cookies are really generated for the logged in url and 
then quitting the driver
"""