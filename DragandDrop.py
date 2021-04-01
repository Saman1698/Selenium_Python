from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class DragandDrop():
    def Drgdp(self):
        driver = webdriver.Chrome(executable_path="C:\\Selenium_Python\\chromedriver.exe")
        url = "https://demoqa.com/droppable"
        driver.maximize_window()
        driver.get(url)  # hit the url

        source = driver.find_element(By.ID, "draggable")
        target = driver.find_element(By.ID, "droppable")
        time.sleep(2)
        action = ActionChains(driver)
        action.drag_and_drop(source,target).perform()
        print("Drag and Drop ...done successfully...!!..")

        driver.close()

dd= DragandDrop()
dd.Drgdp()
  