from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




class Cowin():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)


    def open_two_new_windows(self,faq,partner):
        faq_element = self.driver.find_element(By.XPATH, faq)
        faq_element.click()
        partners_element = self.driver.find_element(By.XPATH, partner)
        partners_element.click()
        return self

    def get_window_ids(self):
        self.window_handles = self.driver.window_handles
        window_ids = []
        for window_id in self.window_handles:
            window_ids.append(window_id)
        return window_ids

    def close_the_opened_windows(self):
        self.driver.switch_to.window(self.window_handles[2])
        self.driver.close()
        self.driver.switch_to.window(self.window_handles[1])
        self.driver.close()


if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    cobject = Cowin(url)
    cobject.open_two_new_windows("(//a[@href='/faq'])[1]","//a[text()=' Partners ']")
    ids = cobject.get_window_ids()
    print("The IDs of the opened windows are as follows : ",ids)
    cobject.close_the_opened_windows()
    print("\nClosed all the opened windows")

"service=Service(ChromeDriverManager().install())"

"""
Using python selenium oops concepts i created a class name Cowin() for the task requested task, where i initiated the driver with the given url "https://www.cowin.gov.in/" through constructor. 
So the task is to open two new windows of diff modules of the site and fetch the window ID of the opened windows and then close them. So i created different methods for all the three tasks. 
Starting with opening two new windows and where i open requested URLs with returning the self and then the second method consists of fetching the window ID of the opened windows through the 
driver. last method will switch to the respective windows and then close them

"""


'''
driver.get("https://www.labour.gov.in/")

documents_link = driver.find_element(By.XPATH,"//a[text()='Documents']")

documents_link.click()

ActionChains(driver).move_to_element(documents_menu).perform()

monthly_report_link = driver.find_element(By.XPATH,"//a[text()='Monthly Progress Report']")

monthly_report_link.click()


february_report_link = driver.find_element(By.XPATH,"//td[text()='February-2024']//following-sibling::td/a")

february_report_link.click()

time.sleep(30)

download_alert = driver.switch_to.alert

download_alert.accept()



chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": "YOUR_DIRECTORY_PATH",
    "download.prompt_for_download": False,
    "plugins.always_open_pdf_externally": True
})

driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL containing the PDF file
driver.get("https://labour.gov.in/sites/default/files/ar_2022_23_english.pdf")

'''