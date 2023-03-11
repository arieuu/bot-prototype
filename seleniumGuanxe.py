from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://guanxe.com/pt/#/8c2a3cc3-3973-43a2-a24a-737b2bbe80e0/fullscreen-initial/page=1&rpp=10")
sleep(5)
element = driver.find_element(By.NAME, "search[query]")
element.send_keys("Iphone X")
sleep(10)

resultGrid = driver.find_elements(By.CLASS_NAME, "dfd-card-title")

for e in range(3):
    print(resultGrid[e].text)
driver.close