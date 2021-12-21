from selenium.webdriver.common.by import By
from selenium import webdriver

#specify driver path
PATH = r'D:\Python\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

import time 

# Results page for software engineer jobs, that are also remote 
driver.get("https://uk.indeed.com/jobs?q=software%20engineer&l=london&remotejob")
 

 
# # Close a modal about finding new jobs 
# driver.find_element_by_xpath("//*[@id='popover-x']/button").click()

# # Advanced search
# driver.find_element_by_xpath("//*[@id='jobsearch']/a").click()

# # Software Engineer jobs 
 
# # 30 results per page 
# driver.find_element_by_xpath("//select[@id='limit']//option[@value='30']").click()
 
# # Sort by date
# driver.find_element_by_xpath("//select[@id='sort']//option[@value='date']").click()

# # Click find job button
# driver.find_element_by_xpath("//*[@id='fj']").click()




time.sleep(5000)
driver.quit()


 