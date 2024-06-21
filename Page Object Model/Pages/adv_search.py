from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Advanced_search:

    def __init__(self,driver):
        self.driver = driver


    def go_to_page(self,url):
        try:
            self.driver.get(url)
            return True
        except:
            print("ERROR : URL is incorrect/Network Error")
            return False

    def handling_modules(self,xpath):
        x = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        ActionChains(self.driver).move_to_element(x).click().perform()
        return True

    def non_clickable_elements(self,element_xpath):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,element_xpath)))
        return element

    def clickable_elements(self,element_xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        ActionChains(self.driver).move_to_element(element).click().perform()

    def check_result(self, result_button, result):
        try:
            see_results_element = self.driver.find_element(By.XPATH, result_button)
            see_results_element.click()
            result = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, result)))
            return result.is_displayed()
        except:
            print("No results were found for the chosen combination")





