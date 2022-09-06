import csv
import requests
import json
from collections import OrderedDict
from time import sleep
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import random

f = open('houseprice.csv','r',encoding="utf-8")
rdr = csv.reader(f)
cnt = 0
whole = []
for a in rdr:
    sleep(1)
    
    id = a[1].replace("https://place.map.kakao.com/","")
    
    req = requests.get(f'https://place.map.kakao.com/main/v/{id}')
    
    source = req.content
    source = json.loads(source.decode('utf-8'))
    #source = str(source).replace("'",'"')
    #source = json.loads(source)
    #print(source)
    info = [cnt]
    if source['isExist']!= False:
        print("going",cnt)

        try:
            info.append(source["basicInfo"]["cid"]),
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["placenamefull"]),
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["phonenum"]),
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["address"]["region"]["fullname"]+source["basicInfo"]["address"]["newaddr"]["newaddrfull"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["homepage"]),
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["category"]["catename"]),
        except:
                info.append(None)
        try:
            info.append(int(source["basicInfo"]["feedback"]["scoresum"]) / int(source["basicInfo"]["feedback"]["scorecnt"]))
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["feedback"]["scorecnt"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["openHour"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["operationInfo"]["appointment"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["operationInfo"]["delivery"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["operationInfo"]["pagekage"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["tags"])
        except:
                info.append(None)
        try:
            info.append(source["menuInfo"])
        except:
                info.append(None)
        try:
            info.append(source["basicInfo"]["mainphotourl"])
        except:
                info.append(None)
        try:
            info.append(source["comment"]["list"])
        except:
                info.append(None)
        try:
            photo_list= []
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            options.add_argument("headless")
            driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
            driver.get(f'https://place.map.kakao.com/{id}')
            sleep(int(random.randrange(5,15)/10))

            driver.find_element(By.XPATH, '//*[@id="mArticle"]/div[4]/div[2]/ul/li[1]/a/span').click()
            sleep(int(random.randrange(5,15)/10))
            for c in range(1,13):
                try:
                    photo = driver.find_element(By.XPATH,f'//*[@id="photoViewer"]/div[2]/div[2]/div/ul/li[{c}]/a/img').get_attribute("src")
                    photo_list.append(photo)
                except:
                    break
            driver.quit()
            info.append(photo_list)
        except:
            info.append(None)

        
        
        
        whole.append(info)
        cnt+=1
        
df = pd.DataFrame(whole)
df.to_csv(f'C:/Users/clehf/CRW/shop_details/whole.csv',index=False)
        

f.close()
