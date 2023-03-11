# Guanxe crawler

import mechanicalsoup

# MechanicalSoup has a stateful browser, meaning it keeps state.
# I can browser here through code and it will remember where I am
# and the things I have done.

browser = mechanicalsoup.StatefulBrowser()

browser.open("https://guanxe.com/pt/")

browser.select_form('form[action="//guanxe.com/pt/pesquisa"]')

browser["search_query"] = "Iphone X"

response = browser.submit_selected() # Make search

print(browser.url)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

