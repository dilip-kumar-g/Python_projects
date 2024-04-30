from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class Drag_drop():

    def __init__(self,url):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(url)

    def switch_to_iframe(self,frame):
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH,frame))

    def fetch_elements(self,drag,drop):
       draggable_element = self.driver.find_element(By.ID,drag)
       droppable_element = self.driver.find_element(By.ID,drop)
       return draggable_element, droppable_element


    def set_action_chains(self,draggable,droppable):
        action = ActionChains(self.driver)
        action.drag_and_drop(draggable, droppable).perform()
        return print("Drag and drop successful")

if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    dd = Dragdrop(url)
    dd.switch_to_iframe("//iframe[@class='demo-frame']")
    x = dd.fetch_elements("draggable","droppable")
    draggable = x[0]
    droppable = x[1]
    dd.set_action_chains(draggable,droppable)


"""
Using python selenium oops concepts i created a class name Drag_drop() for the task requested task, where i initiated the driver with the given url "https://jqueryui.com/droppable/" through constructor. 
So the task is to drag and drop an element from the page successfully. I have created 4 methods for the same, 1st one is to launch the browser with the given URL through the webdriver.

Second method is to switch the driver to the iframe where the drag drop element is present and the 3rd one is to fetch the elements of the drag and drop. 

and the final one is to import the Action chains module and implement the same into the driver and then finally to perform the drag drop action

"""
