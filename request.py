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


firstResult = getResponse("https://ows.goszakup.gov.kz/trd-buy/bin/130940015918");
next_page = firstResult['next_page'];

flag = True;

array = [];
array.append(next_page);

while True:
    result = getResponse("https://ows.goszakup.gov.kz" + next_page);
    next_page = result['next_page'];

    array.append(next_page);

    if not next_page:
        break;

pprint(len(array));
pprint(firstResult)



