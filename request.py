import requests
import urllib3
from pprint import pprint
import json


urllib3.disable_warnings()

def getResponse(url):


        payload = "";
        headers = {
            'Authorization': "Bearer b6dd1aa395a9e875a7d63ab380c65fb5",
            'cache-control': "no-cache",
            'Postman-Token': "852c66bb-7400-4461-8e4f-8a44e9465c3c"
        }

        response = requests.request("GET", url, data=payload, headers=headers, verify=False);

        return json.loads(response.text);


arrayObject = [];


class Customers(object):
    name = ""
    email = 0
    phone = ""
    type = 0
    website = ""

def make_customer(name, email="", phone="", type=0, website=""):
    customer = {};
    customer = {'name': name,
           "email": email,
           "phone": phone,
           "type": type,
           "website": website};


    return customer

def addObject(result):
    for rec in result['items']:

        name = ""
        email = ""
        phone = ""
        type = ""
        website = ""

        if 'name_ru' in rec:
            name = rec['name_ru'];

        if 'email' in rec:
            email = rec['email'];

        if 'phone' in rec:
            phone = rec['phone'];

        if 'type_supplier' in rec:
            type = rec['type_supplier'];

        if 'website' in rec:
            website = rec['website'];

        arrayObject.append(make_customer(name, email, phone, type, website));


result = getResponse("https://ows.goszakup.gov.kz/subject/all");
addObject(result)

next_page = result['next_page'];

while True:
    result = getResponse("https://ows.goszakup.gov.kz" + next_page);

    if not next_page:
        break;

    addObject(result)
    pprint(len(arrayObject))


