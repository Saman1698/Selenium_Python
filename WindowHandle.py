from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
#
# class HandleWindows():
#     def hw(self):
driver = webdriver.Chrome(executable_path="C:\\Selenium_Python\\chromedriver.exe")
url = "https://demoqa.com/browser-windows"       # parent window
driver.maximize_window()
driver.get(url)  # hit the url
print("You hit the url")

driver.find_element(By.ID, "windowButton").click()
time.sleep(2)
print("....new window hit!")

main = driver.current_window_handle  # handle current window
handles = driver.window_handles

print(driver.title)  # Current window title

handles = driver.window_handles
for h in handles:
    driver.switch_to.window(h)
    print(driver.title)

# win = HandleWindows()
# win.hw()












