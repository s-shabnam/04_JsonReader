#Extracts data from json file
#espextec input form :
# input'''
#[
#   {        name: 'Matthias'        count: 97    },
#   {        name: 'Geomer'        count: 97    }
#]'''

import json
from urllib.request import Request, urlopen

while True:
    jsonFileURL = input('Enter json file url - ')
    if len(jsonFileURL) < 1 :
    #default json adress
        jsonFileURL = 'http://python-data.dr-chuck.net/comments_345027.json'

    jsonFile = urlopen(jsonFileURL).read().decode('utf-8')

    print('Json file URL: ', jsonFileURL)
    #print('Json file: ', jsonFile)
    try:
        info = json.loads(jsonFile)
    except:
        print('Json data extraction problem occured.')
        exit()

    print('User count:', len(info))

    total = 0
    for item in info:
        if item == "comments":
            innerJsonList = info[item]
           # print(innerJsonList)
            print (type(innerJsonList))
            for element in innerJsonList:
                #print(element['count'])
                total= total + element['count']

    print(total)