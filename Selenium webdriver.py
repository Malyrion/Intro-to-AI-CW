from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

import pandas as pd 

# Chrome driver path that is needed for Selenium
PATH = r'D:\Python\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Results page for software engineer jobs, that are also remote 

# Data we are collecting 
companies=[]
titles=[]
salaries=[]
addresses=[]
# remote=[] Temporarily commenting this since remote state needs to be read from Location
ratings=[]
jobDescription=[]

# @Todo for next push [Neeraj]
# Boolean for part time or not, 0 being part time 1 for full time after cleaning
workingHours=[] 
jobDescriptionLong=[] # seeing if longer job descriptions have salary

# url loads 50 results of software jobs in London 
# loop is used to step through the number of results, [50, 100, 150, etc]
# 500 job results are checked with (0, 10) since 50 results of 10 pages will be checked

for i in range(0, 10):
    url = 'https://uk.indeed.com/jobs?q=software%20engineer&l=london&limit=50&start'
    url += str(50*i)
    driver.get(url) 
    jobs = driver.find_elements_by_class_name('tapItem')
    for job in jobs:
        companies.append(job.find_element_by_class_name('companyName').text)
        titles.append(job.find_element_by_class_name('jobTitle').text)
        addresses.append(job.find_element_by_class_name('companyLocation').text)
        # ratings.append(job.find_element_by_class_name('ratingLink').text) @Todo [Neeraj]
        try: 
            salary = job.find_element_by_class_name('salary-snippet-container').text
            salaries.append(salary)
        except NoSuchElementException:
            salaries.append('None')

        jobDescription.append(job.find_element_by_class_name('job-snippet').text)  
    

res = pd.DataFrame({'Title': titles,'Company': companies, 'Address': addresses, 'Salary': salaries, 'Job description': jobDescription})
print(res)
res.to_csv('data.csv')
 
