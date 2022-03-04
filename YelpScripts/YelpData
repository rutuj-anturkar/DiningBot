# -*- coding: utf-8 -*-
"""YelpData.ipynb"""

import requests
API_KEY = "_IfbP0nEMBHm1IOAAgvxEYHfsl1csUIcXQ-lrSMIS_8M81mH0OW-2Gd5D8SfP6nNxv2neg2dab9I1GYN7Fr2c6A1uN1JWTRMcXDV5zyWr62sSBU78OUbir69BAUhYnYx"

import json
import time

ENDPOINT = "https://api.yelp.com/v3/businesses/search"
HEADERS = {'Authorization': 'bearer %s' % API_KEY , 'User-Agent': 'PostmanRuntime/7.28.4'}

PARAMETERS = {'term': 'Chinese',
             'limit': 50,
              'offset': 0,
             'radius': 10000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Chinesedata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)

with open('Chinesedata.json') as json_file:
    data = json.load(json_file)
    print(len(data))

PARAMETERS = {'term': 'Indian',
             'limit': 50,
              'offset': 0,
             'radius': 20000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Indiandata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)

with open('Indiandata.json') as json_file:
    data = json.load(json_file)
    print(len(data))

PARAMETERS = {'term': 'Thai',
             'limit': 50,
              'offset': 0,
             'radius': 20000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Thaidata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)

PARAMETERS = {'term': 'Italian',
             'limit': 50,
              'offset': 0,
             'radius': 20000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Italiandata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)

PARAMETERS = {'term': 'Mexican',
             'limit': 50,
              'offset': 0,
             'radius': 20000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Mexicandata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)

PARAMETERS = {'term': 'American',
             'limit': 50,
              'offset': 0,
             'radius': 20000,
             'location': 'Manhattan'
             }

i = 1
fop = []
status_code = 200
while status_code==200:
    response = requests.get(url= ENDPOINT, params = PARAMETERS, headers = HEADERS)
    print(str(i)+" "+str(response.status_code))
    status_code = response.status_code
    business_data = response.json()
    if response.status_code==200:
            for biz in business_data['businesses']:
                output = {}
                output['id'] = biz['id']
                output['name'] = biz['name']
                output['cuisine'] = biz['categories']
                output['contact'] = biz['phone']
                output['address'] = ", ".join(biz['location']['display_address'])
                output['zipcode'] = biz['location']['zip_code']
                output['coordinates'] = biz['coordinates']
                output['reviewcount'] = biz['review_count']
                output['rating'] = biz['rating']
                fop.append(output)
    PARAMETERS['offset'] = PARAMETERS['offset']+50
    time.sleep(2)
    i = i+1
    
print(fop)
with open("Americandata.json","a") as jsonFile:
    json.dump(fop, jsonFile, indent=4)
