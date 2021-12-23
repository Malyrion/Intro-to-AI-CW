# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 00:34:15 2021

@author: Lolpin
"""

import json
import csv
from io import StringIO
from geopy.distance import geodesic

def distanceFromCentralLondon(latitudeString, longitudeString):
    central = (51.507391,-0.127700)   
    return geodesic((latitudeString, longitudeString), central).kilometers

with open('glassdoorSoftwareEngineer1.json', encoding='utf-8') as json_data:
    data = json.load(json_data)

with open('glassdoorSoftwareEngineer1.csv', 'w', newline='', encoding='utf-8') as csv_out:
    csvwriter = csv.writer(csv_out)
    csvwriter.writerow(["jobListingId","jobTitle","jobCategory-FullTime","jobRemote","kilometerDistanceFromCentral"])
    # title (categorical), full-time(bool), 
    # remote(bool), salary(integer),distanceToCenter(integer)
    
    print(data['response']['jobListings'])
    
    for jobListing in data['response']['jobListings']:
        jobListingId = jobListing["jobListingId"]
        jobTitle = jobListing["normalizedJobTitle"]
        jobCategory = jobListing["jobCategory"]
        
        #semi-colon separated string value for jobSourceAdTarget
        #take json parsed element in as file via stringIO into list
        csvreader = csv.reader(StringIO(jobListing["jobSourceAdTarget"]), delimiter=';')
        jobDetailsList = list(csvreader)
        jobRemote = jobDetailsList[0][15]
        
        locLat = (jobDetailsList[0][11]).partition("=")[2]
        locLong = (jobDetailsList[0][12]).partition("=")[2]
        distanceFromCentral = distanceFromCentralLondon(locLat,locLong)
        
        csvwriter.writerow([jobListingId, jobTitle, jobCategory, jobRemote, distanceFromCentral])
        
