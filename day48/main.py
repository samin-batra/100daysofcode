from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\Users\\samin\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

lis = driver.find_element(by = By.XPATH, value = '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events = lis.find_elements(by = By.TAG_NAME, value="li")
print(events[0].text)
event_details = dict()

for i in range(0, len(events)):
    e = events[i].text
    event_details[i] = {"name": e.split("\n")[1], "time": e.split("\n")[0]}
print(event_details)
# event_names = {}


print()


driver.quit()

