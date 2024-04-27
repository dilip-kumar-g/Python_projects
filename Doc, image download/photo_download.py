import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Pic_download():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)

    def navigate_to_gallery(self,media,press,gallery,images):
        media_button = self.driver.find_element(By.XPATH, media)
        media_button.click()
        more_info = self.driver.find_element(By.XPATH, press)
        more_info.click()
        photo_gallery = self.driver.find_element(By.XPATH, gallery)
        photo_gallery.click()
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[1])
        images = self.driver.find_elements(By.XPATH, images)
        return images

    def create_download_directory(self,name):
        os.mkdir(name,exist_ok=True)

    def download_photos(self,numbers,images):
        for index, image in enumerate(images):
            if index < numbers:
                image_url = image.get_attribute("src")
                if image_url:
                    response = requests.get(image_url)
                    if response.status_code == 200:
                        with open(f"photos/image{index + 1}.jpg", "wb") as photo:
                            photo.write(response.content)

if __name__ == "__main__":
    url = "https://www.labour.gov.in/"
    down = Pic_download(url)
    images = down.navigate_to_gallery("//a[text()='Media']","//a[text()='Click for more info of Press Releases']","//a[text()='Photo Gallery ']","//img[@typeof='foaf:Image']")
    down.create_download_directory("photos")
    down.download_photos(10,images)
    print("Images downloaded successfully ")


"""

Using python selenium oops concepts i created a class name Pic_download() for the task requested task, where i initiated the driver with the given url "https://www.labour.gov.in/" through constructor. 
So the task is to download the first 10 images present in the photo gallery section. I had split the task into 3 method for 3 diff sections of the task. In the first method i will get navigated to the photo
gallery section from the home page and handle the browser to the respective window, also will fetch all the images and save them in a variable and get them returned from the first method.

Second method is to created the directory for the images to be downloaded and also to check if there is already a path/folder present of the requested name. 

Third method is to ge the images elements from the first method and iterate over the desired no of images wish to be downloaded

from the main , created an object named down and then called all the 3 methods one by with appropriate arguments and downloaded 10 images as per the request.


"""


