import requests
import  json
import configparser
from requestjson import *

from Utilities.configuration import *
from Utilities.resources import *
from requests.auth import HTTPBasicAuth

from HomePage.requestjson import request_input
url = getconfig()['API']['endpoint'] + apiendpoints.endpoint
headers={'content-type':'application/json'}
shipment_response= requests.post(url,
              json=request_input("US"),auth=HTTPBasicAuth(username='EZTK0126bfcd0c834208b2289e3c501630d7IMAAxVrGZ2G1UXCmomm4Pw',password=''),
             params={'ShipmentId':'shp_e0b570fd1d7d4b62bd206917eae5881a'},headers=headers)
# print(shipment_response.json())
shipment_id= shipment_response.json()['id']
shipment_country= shipment_response.json()['country']
print(shipment_id,shipment_country)

