from http.client import RemoteDisconnected
import requests
from datetime import datetime

TARGET_URL = "https://api-0.752628.xyz/ip"

for i in range(100000):
    try:
        start_time = datetime.now()
        response = requests.get(TARGET_URL)
        print(i, str(datetime.now() - start_time), response.status_code, response.text)
    except RemoteDisconnected as e:
        print(i, str(datetime.now() - start_time), "FAILED")