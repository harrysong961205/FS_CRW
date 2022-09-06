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

#위치
where_list = ["홍대"]

#종류
food_type = ["삼겹살","초밥","스테이크","오겹살","등갈비 김치찜","회","곱창","김치찌개","치킨","돼지갈비","대게","킹크랩","라면","육회","소갈비","떡볶이","랍스터","간장게장","곱창","감자탕","된장찌개","샤브샤브","부대찌개","햄버거","항정살","훈제삼겹살","닭발","뼈다귀 해장국"]




food_href_list = []
for a in where_list:
    for b in food_type:
        
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
        driver.get('https://map.kakao.com/')
        driver.find_element(By.XPATH,'//*[@id="search.keyword.query"]').send_keys(a+" "+b)
        driver.find_element(By.XPATH, '//*[@id="search.keyword.submit"]').send_keys(Keys.ENTER)
        sleep(1)
        #키워드 엔터 후 접속


        done = True
        while done:
            try:
                pageSource = driver.find_elements(By.CLASS_NAME,'moreview')
                for i in range(len(pageSource)):
                    food_href_list.append(pageSource[i].get_attribute("href"))

                driver.find_element(By.XPATH, '//*[@id="info.search.place.more"]').send_keys(Keys.ENTER)
                
            except:
                break
            cnt =3
            while True:
                #food_href_list.append("here!")
                try:
                    sleep(1)
                    pageSources = driver.find_elements(By.CLASS_NAME,'moreview')
                    for i in range(len(pageSources)):
                        food_href_list.append(pageSources[i].get_attribute("href"))
                except:
                    print("목록 실패")
                    done= False
                    break


                if cnt ==6:
                    if driver.find_element(By.XPATH, f'//*[@id="info.search.page.next"]').get_attribute('class')!="next":
                        done= False
                        break
                    
                    driver.find_element(By.XPATH, f'//*[@id="info.search.page.next"]').send_keys(Keys.ENTER)
                    sleep(1)
                    cnt= 2
                    continue
                    


                try:
                    driver.find_element(By.XPATH, f'//*[@id="info.search.page.no{cnt}"]').send_keys(Keys.ENTER)
                    sleep(1)
                except:
                    print("다음으로 넘어가기 실패", len(food_href_list))
                    print(cnt)
                    done= False
                    break
                cnt+=1
                print(cnt)
                    
        
        


        
            
        

        
        
        driver.quit()

df = pd.DataFrame(food_href_list)

df.to_csv("houseprice.csv")


