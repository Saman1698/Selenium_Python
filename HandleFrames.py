from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class HandleFrames():
    def hfrm(self):
        driver = webdriver.Chrome(executable_path="C:\\Selenium_Python\\chromedriver.exe")
        url = "https://letskodeit.teachable.com/p/practice"
        driver.maximize_window()
        driver.get(url)  # hit the url

        # switch to first frame
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='courses-iframe']"))
        header_1 = driver.find_element_by_tag_name("input")
        header_1.send_keys("Selenium webdriver with python")
        search = driver.find_element_by_xpath("//i[@title='Search']")
        search.click()
        time.sleep(2)
        print("You switched to first frame..!!")


        # switch back to default content
        driver.switch_to.default_content()
        print("You switched back to default content..!!")

        click_on_term_of_use = driver.find_element_by_partial_link_text("Terms of U")
        click_on_term_of_use.click()
        time.sleep(2)
        print("you clicked on term of use...!!!!")

        # # switch to second frame
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='frame2']"))
        # header_2 = driver.find_element(By.CSS_SELECTOR, "#sampleHeading").text
        # print("You switched to second frame...!!")
        # print(header_2)


        driver.quit()

hf= HandleFrames()
hf.hfrm()
