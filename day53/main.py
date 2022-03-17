from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys




chrome_driver_path = ""

gform_link = "https://forms.gle/wAeVN3D3pmNsqGt86"

html = requests.get("https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69219435644531%2C%22east%22%3A-122.17446364355469%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D", headers={"Accept-Language":"en-US,en;q=0.9","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"})
#
# print(html.content)

bs = BeautifulSoup(html.content, 'html.parser')

# print(bs.prettify())

info =  bs.find_all(name="div",attrs={"class":"list-card-info"})
links = []
prices = []
addresses = []


# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get(gform_link)
# time.sleep(2)

for i in info:
    # price = driver.find_element(by = By.XPATH, value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    #
    # link = driver.find_element(by=By.XPATH,
    #                             value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
    # address = driver.find_element(by=By.XPATH,
    #                             value="//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")

    l = i.find(name="a",attrs={"class":"list-card-link"})
    p = i.find(name="div", attrs={"class": "list-card-price"})
    a = i.find(name="address", attrs={"class": "list-card-addr"})

    if l is not None and p.string is not None and a.string is not None :
        print(f"Link: {l['href']}")
        print(f"Price: {p.string}")
        print(f"Address: {a.string}")
        if "https://www.zillow.com/" not in l['href']:
            links.append("https://www.zillow.com" + l['href'])
        else:
            links.append(l['href'])
            # link.send_keys(l['href'])
        # print(p.string)
        prices.append(p.string)
        # price.send_keys(p.string)
        # # print(a.string)
        addresses.append(a.string)
        # address.send_keys(a.string)
        # button = driver.find_element(by = By.CSS_SELECTOR, value="div[role=button]")
        # button.click()
        # time.sleep(2)
        # submit_another = driver.find_element(by = By.LINK_TEXT, value="Submit another response")
        # submit_another.click()
        # time.sleep(3)
    # driver.close()

print(f"Prices: {prices}")
print(f"Addresses: {addresses}")
print(f"Links: {links}")




