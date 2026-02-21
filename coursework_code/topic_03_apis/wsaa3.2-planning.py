# get planning applications
# Author: Tihana Gray

import requests
url= "https://opendata.arcgis.com/datasets/8f69dffe26324ba3acc653cf6cb5cf8b_0.geojson"
response = requests.get(url)
list_of_planning = response.json()
print (response.status_code)

print(list_of_planning["features"][0]["geometry"]["coordinates"])
# continuously getting connection error, not sure why. I have tried to run the code several times but it keeps giving me the same error. I will try to find a solution to this problem.