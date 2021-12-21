from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import pandas as pd 

#specify driver path
PATH = r'D:\Python\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

import time 

# Results page for software engineer jobs, that are also remote 
driver.get("https://uk.indeed.com/jobs?q=software%20engineer&l=london&remotejob")
 

# Data we are collecting 
companies=[]
titles=[]
salaries=[]
addresses=[]
# Boolean for part time or not, 0 being part time 1 for full time after cleaning
workingHours=[]
remote=[]
reviews=[]
jobDescription=[]

descriptions=[]

time.sleep(3000)

jobs = driver.find_elements_by_class_name('tapItem')
for j in jobs:
    companies.append(j.find_element_by_class_name('companyName').text)
    titles.append(j.find_element_by_class_name('jobTitle').text)
    addresses.append(j.find_element_by_class_name('companyLocation').text)

    try: 
        salary = j.find_element_by_class_name('salary-snippet-container')
        salaries.append(salary)
    except NoSuchElementException:
        salaries.append("None")

    jobDescription.append(j.find_element_by_class_name('job-snippet').text)   



# results = pd.DataFrame({"job_title": titles,"company": companies})
# results.head()
 
driver.quit()