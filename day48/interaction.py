import time

from selenium import webdriver
from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\\Users\\samin\\chromedriver_win32\\chromedriver.exe"
#
driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# articles = driver.find_element(by = By.XPATH,value = '//*[@id="articlecount"]/a[1]')
#
# print(articles.text)
#
# driver.quit()


# driver.get("http://secure-retreat-92358.herokuapp.com/")
#
# fname = driver.find_element(by = By.NAME, value="fName")
# # driver.find_element_by_name("fName")
# lname = driver.find_element(by = By.NAME, value="lName")
# email = driver.find_element(by = By.NAME, value="email")
#
# fname.send_keys("Samin")
# lname.send_keys("Batra")
# email.send_keys("saminba@sjjsjsj.cmo")
# email.send_keys(Keys.ENTER)
#
# time.sleep(5)
#
# message = driver.find_element(by = By.CLASS_NAME, value="display-3")
# m = message.text
#
# print(m)



driver.get("https://www.linkedin.com/feed/")

# jobs = driver.find_element(by = By.LINK_TEXT,value="Jobs")

# email_input.send_keys("sb661@snu.edu.in")
# pass_input.send_keys("Saveusy2j29!")

sign_in = driver.find_element(by = By.LINK_TEXT,value="Sign in")
sign_in.click()


time.sleep(5)


email_input = driver.find_element(by=By.NAME,value="session_key")
pass_input = driver.find_element(by = By.NAME, value="session_password")
email_input.send_keys("sb661@snu.edu.in")
pass_input.send_keys("Saveusy2j!")

submit_button = driver.find_element(by = By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')

submit_button.click()
time.sleep(5)

jobs_link = driver.find_element(by = By.XPATH,value='//*[@id="ember20"]')

jobs_link.click()
time.sleep(4)

job_title = driver.find_element(by = By.CSS_SELECTOR, value='#jobs-search-box-keyword-id-ember277')
job_title.send_keys("python developer")
job_title.send_keys(Keys.ENTER)

# driver.quit()