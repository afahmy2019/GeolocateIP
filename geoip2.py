import requests
import pprint
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Supress warnings
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

ip_address = input("Enter the IP Address to look up: ")

url = "https://api.iplocation.net/?ip=" + ip_address

response = requests.request("GET", url, verify=False)

pprint.pprint(response.json())
