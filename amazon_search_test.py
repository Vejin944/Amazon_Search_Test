from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



#Create a variable "driver" and input absoulte path

driver = webdriver.Chrome(executable_path='/Users/mac/Desktop/Amazon_test/venv/chromedriver-Darwin')
#Wait 5 seconds
driver.implicitly_wait(5)
#Find web adress
driver.get('https://www.amazon.com/')

#Search for find field
search = driver.find_element_by_id(By.ID, id = 'twotabsearchtextbox')
#Input text "dress"
search.send_keys('dress', Keys.ENTER)
