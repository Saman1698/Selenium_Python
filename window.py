from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Selenium_Python\\chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL
driver.get("https://the-internet.herokuapp.com/windows")
#to refresh the browser
driver.refresh()
driver.find_element_by_link_text("Click Here").click()
#prints the window handle in focus
print(driver.current_window_handle)
#to fetch the first child window handle
chwnd = driver.window_handles[1]
#to switch focus the first child window handle
driver.switch_to.window(chwnd)
print(driver.find_element_by_tag_name("h3").text)
#to close the browser
driver.quit()