from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd 
import numpy as np 

# Chrome driver path that is needed for Selenium
PATH = r'D:\Python\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

# Results page for software engineer jobs, that are also remote 

# Data we are collecting 
companies=[]
titles=[]
salaries=[]
addresses=[]
# remote=[] Not needed anymore since its derived from location
ratings=[]
jobDescription=[]

# Boolean for part time or not, 0 being part time 1 for full time after cleaning
# workingHours=[] 
jobLink=[] # seeing if longer job descriptions have salary

# url loads 50 results of software jobs  
# loop is used to step through the number of results, [50, 100, 150, etc]

for i in range(0, 10):
    url = 'https://uk.indeed.com/jobs?q=software%20engineer&limit=50&start='
    url += str(50*i)
    driver.get(url)
 
    try:
        tapLoaded = EC.presence_of_element_located((By.CLASS_NAME, 'tapItem'))
        WebDriverWait(driver, 3).until(tapLoaded)
    except TimeoutException:
        print('Timeout for waiting more than three seconds')
    finally:
        print('Tap items loaded properly')

    jobs = driver.find_elements_by_class_name('tapItem')
    for job in jobs:
        # url = 'https://uk.indeed.com/jobs?q=software%20engineer&limit=50&start&vjk=' + job.get_attribute('id')
        # Can use the code above by setting up another driver for fetching each job requirement 

        try: 
            salary = job.find_element_by_class_name('salary-snippet-container').text
            salaries.append(salary)

            jobLink.append(job.get_attribute('href'))
         
            # try: 
            #     fullTime = job.find_element_by_class_name('jobsearch-JobInfoHeader-title-container').text
            #     workingHours.append(fullTime)
            # except NoSuchElementException:
            #     workingHours.append('None')
            try: 
                company = job.find_element_by_class_name('companyName').text
                companies.append(company)
            except NoSuchElementException:
                companies.append('')

            titles.append(job.find_element_by_class_name('jobTitle').text.replace("new", "").replace("\n", ""))
                # spliting cases with remote jobs using comma delimiter, removing "•" and "+1 location" link which is not helpful as there is another record with same post but different location
            addresses.append(job.find_element_by_class_name('companyLocation')
            .text.replace("•", " ")
            .replace("\n", "")
            .replace("+1 location", "")
            .replace("+2 locations", "")
            .replace("+3 locations", "")
            .replace("+4 locations", "")
            .replace("+5 locations", "")
            .rstrip(","))

            try: 
                rating = job.find_element_by_class_name('ratingNumber').text
                # print(rating) debug
                ratings.append(rating)
            except NoSuchElementException:
                ratings.append('')


            jobDescription.append(job.find_element_by_class_name('job-snippet').text)

        except NoSuchElementException:
            continue

res = pd.DataFrame({'Title': titles,'Company': companies, 'Links': jobLink, 'Ratings': ratings, 'Address': addresses, 'Salary': salaries, 'Job description': jobDescription})
print(res)
res.to_csv('data.csv')
 
