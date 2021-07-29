import time
from selenium import webdriver
import selenium

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

driver.get('https://www.google.com/?gws_rd=ssl')

time.sleep(1)

searchbutton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
searchbutton.send_keys('Sololearn')

time.sleep(1)

clickbutton = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
clickbutton.click()
time.sleep(1)