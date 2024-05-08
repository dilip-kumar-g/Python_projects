from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Imdb():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(url)

    def handling_modules(self,xpath):
        x =  WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,xpath)))
        ActionChains(self.driver).move_to_element(x).click().perform()

    def accessing_elements(self,element_xpath):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,element_xpath)))
        return element

    def accessing_clickable_elements(self,element_xpath):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
        ActionChains(self.driver).move_to_element(element).click().perform()



    def check_result(self,result_button,result):
        try:
            see_results_element = self.driver.find_element(By.XPATH, result_button)
            see_results_element.click()
            result = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, result)))
            print(result.is_displayed())
        except:
            print("No results were found for the chosen combination")


if __name__ == "__main__":
    url = "https://www.imdb.com/search/name/"
    imdb = Imdb(url)
    imdb.handling_modules("(//span[@class='ipc-accordion__item__chevron'])[1]")
    name_input_element = imdb.accessing_elements("//input[@name='name-text-input']")
    name_input_element.send_keys("Tom")
    imdb.handling_modules("(//span[@class='ipc-accordion__item__chevron'])[2]")
    from_date_element = imdb.accessing_elements("//input[@name='birth-date-start-input']")
    from_date_element.send_keys("07/07/1900")
    to_date_element = imdb.accessing_elements("//input[@name='birth-date-end-input']")
    to_date_element.send_keys("07/05/2024")
    imdb.handling_modules("(//span[@class='ipc-accordion__item__chevron'])[4]")
    imdb.accessing_clickable_elements("//button[@data-testid='test-chip-id-oscar_best_actor_nominees']")
    imdb.handling_modules("(//span[@class='ipc-accordion__item__chevron'])[5]")
    imdb.accessing_clickable_elements("//button[@data-testid='test-chip-id-BIOGRAPHY']")
    imdb.handling_modules("(//span[@class='ipc-accordion__item__chevron'])[7]")
    male_button = imdb.accessing_clickable_elements("//button[@data-testid='test-chip-id-MALE']")
    imdb.check_result("//span[text()='See results']","(//ul)[14]")
