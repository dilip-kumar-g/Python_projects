from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service




class Instagram():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)

    def get_followers_count(self,followers):
        followers_element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,followers)))
        followers_count = followers_element.get_attribute("title")
        return followers_count

    def get_following_count(self,following):
        following_element = self.driver.find_element(By.XPATH,following)
        following_count = following_element.text
        return following_count


if __name__ == '__main__':
    url = "https://www.instagram.com/guviofficial/"
    insta = Instagram(url)
    followers =insta.get_followers_count("//button[@class=' _acan _acao _acat _aj1- _ap30']//span[@title]")
    following = insta.get_following_count("//button[text()=' following']/span/span[text()]")
    print("Total followers of Guvi official page is:", followers)
    print("Total no of people following Guvi are :", following)


"""

Using python selenium OOPS concepts i created a class name instagram() for the task requested task, where i initiated the driver with the given url "https://www.instagram.com/guviofficial/" through constructor. 
So the task is to get the no of instagram users following Guvi official page and no of users Guvi official page is following. for this i created two methods to get the followers and no of following count from each
method. to get the followers count i am first getting the element and the value of the attribute "title" where the followers count is present and also for the following count i am fetching the same element and get 
text values of it. from the main i will print all the values and display the output.

I have picked relative XPath for both the values 

"""






