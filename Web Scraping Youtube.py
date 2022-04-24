#!/usr/bin/env python
# coding: utf-8

# # Webscraping de vídeos do Youtube com Python

# In[1]:


from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()


# In[24]:


driver.get('https://www.youtube.com/')

time.sleep(1)
driver.find_element(By.NAME, 'search_query').send_keys('python')
driver.find_element(By.NAME, 'search_query').send_keys(Keys.ENTER)


# In[26]:


for i in range(20):
    scroll = i * 10000
    driver.execute_script(f"window.scroll(0, {scroll});")
    time.sleep(2)

videos = driver.find_elements(By.ID, 'thumbnail')

for video in videos:
    print(video.get_attribute('href'))


# In[33]:


len(videos)
import pandas as pd
df = pd.DataFrame(videos, columns=["Videos"])
df.to_excel("videos.xlsx")

