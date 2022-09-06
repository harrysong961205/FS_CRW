from cgitb import html
from email import contentmanager
import os
import site
from time import sleep
from bs4 import BeautifulSoup
import requests
import os
from time import sleep
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

url = 'https://place.map.kakao.com/2122076929'

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
driver.get(url)
sleep(3)
merchant_name = driver.find_element(By.XPATH,'//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/h2')
#print("1111")
print(merchant_name.text)
rate =driver.find_element(By.XPATH,"//*[@id='mArticle']/div[1]/div[1]/div[2]/div/div/a[1]/span[1]")
print(rate.text)
review_number = driver.find_element(By.XPATH,'//*[@id="mArticle"]/div[1]/div[1]/div[2]/div/div/a[2]/span')
print(review_number.text)
address_name = driver.find_element(By.CLASS_NAME,"txt_address")
print(address_name.text)
