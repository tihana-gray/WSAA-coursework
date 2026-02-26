import requests
import urllib.parse
from config import config as cfg

targetUrl = "https://andrewbeatty1.pythonanywhere.com/bookviewer.html"
apiKey = cfg["htmltopdfkey"]

apiurl = 'https://api.html2pdf.app/v1/generate'
params = {'url': targetUrl, 'apiKey': apiKey}
parsedparams = urllib.parse.urlencode(params)
requestUrl = apiurl + "?" + parsedparams

response = requests.get(requestUrl)
print(response.status_code)

result = response.content

with open(r"C:\Users\tihan\OneDrive\Desktop\ATU\WSAA-coursework\labs\Lab04.02_APIkeys\document.pdf", "wb") as handler:
    handler.write(result)