from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd 
# Chrome driver path that is needed for Selenium
PATH = r'D:\Python\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(PATH)

jobs = pd.read_csv('data.csv')


def url_to_desc(x):
     
    url = x
    driver.get(url)

    try:
        tapLoaded = EC.presence_of_element_located((By.CLASS_NAME, 'test'))
        WebDriverWait(driver, 3).until(tapLoaded)
    except TimeoutException:
        print('Timeout for waiting more than three seconds')
    finally:
        print('Tap items loaded properly')

    try:
        jobdesclong = driver.find_element_by_class_name('jobsearch-JobComponent-description').text
        return jobdesclong 
    except NoSuchElementException:
        return ""
        
jobs['full-description'] = jobs['Links'].map(url_to_desc)
jobs.to_csv('data.csv')