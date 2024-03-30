
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")


login_button = driver.find_element(By.XPATH, "//input[@id='login-button']")
username = driver.find_element(By.XPATH, "//input[@id='user-name']")
password = driver.find_element(By.XPATH, "//input[@id='password']")


username.send_keys("standard_user")
password.send_keys("secret_sauce")
login_button.click()

print("The title of the webpage is: ", driver.title)

print('The current URL of the webpage is:',driver.current_url)

with open('page_source.txt','w') as file_object:
    file_object.write(driver.page_source)

with open('page_source.txt') as objects:
    contents = objects.read()
    print("The contents present in the webpage which is saved in the file is: \n\t",contents)

driver.quit()
