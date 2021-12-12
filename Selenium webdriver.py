from selenium.webdriver.common.by import By
from selenium import webdriver

#specify driver path
PATH = r'C:\Users\44757\Documents\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

import time 

#indeed

# Input Software Engineer in jobs field
driver.get("https://uk.indeed.com/?r=us")
driver.find_element_by_xpath("//*[@id='text-input-what']").send_keys("Software Engineer")


# Input United Kingdom in Where field
driver.find_element_by_xpath("//*[@id='text-input-where']").send_keys("United Kingdom")


# Jobs search button 
driver.find_element_by_xpath("//*[@id='jobsearch']/button").click()
 
# # Close a modal about finding new jobs 
# driver.find_element_by_xpath("//*[@id='popover-x']/button").click()

# Advanced search
driver.find_element_by_xpath("//*[@id='jobsearch']/a").click()

# Software Engineer jobs 
 
# 30 results per page 
driver.find_element_by_xpath("//select[@id='limit']//option[@value='30']").click()
 
# Sort by date
driver.find_element_by_xpath("//select[@id='sort']//option[@value='date']").click()

# Click find job button
driver.find_element_by_xpath("//*[@id='fj']").click()




time.sleep(5000)
driver.quit()


 