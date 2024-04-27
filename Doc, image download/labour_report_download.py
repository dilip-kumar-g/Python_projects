from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Reports():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)

    def go_to_reports(self,docs,reports,report):
        documents_menu = self.driver.find_element(By.XPATH, docs)
        ActionChains(self.driver).move_to_element(documents_menu).perform()
        monthly_report = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable((By.XPATH,reports)))
        monthly_report.click()
        report_link = self.driver.find_element(By.XPATH, report)
        report_link.click()
        download_alert = self.driver.switch_to.alert
        download_alert.accept()
        return self

    def get_report_url(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        report_url = self.driver.current_url
        return report_url

    def add_chrome_options_and_download(self,report_url):
        chrome_options = Options()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": "YOUR_DIRECTORY_PATH",
            "download.prompt_for_download": False,
            "plugins.always_open_pdf_externally": True
        })
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(report_url)


if __name__ == "__main__":
    url = "https://labour.gov.in/"
    reports = Reports(url)
    reports.go_to_reports("//a[text()='Documents']","//a[text()='Monthly Progress Report']","//td[text()='February-2024']//following-sibling::td/a")
    report_url = reports.get_report_url()
    reports.add_chrome_options_and_download(report_url)


"""

Using python selenium oops concepts i created a class name Reports() for the task requested task, where i initiated the driver with the given url "https://labour.gov.in/" through constructor. 
So the task is to go to the reports section and download the monthly status report. So i created different methods for to do the task in 3 steps, one is to navigate to the monthly reports section,
in the second one we will fetch the URL of the desired report from the new window that is opened for download, third one is to add the chrome options for the download preferences as just clicking on the 
download icon will not initiate download since the file will be opened in the new window as pdf viewer and we need to set preferences for the browser options for path, prompt for download. From the main file
with creating the object i had called all the 3 methods and downloaded the report successfully.

"""
