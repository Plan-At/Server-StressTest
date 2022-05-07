from http.client import RemoteDisconnected
import requests
from datetime import datetime

TARGET_URL = "https://api.752628.xyz/ip"
REUSE_CLIENT = True

http_client = requests.Session()
for i in range(100000):
    start_time = datetime.now()
    if REUSE_CLIENT:
        http_client = http_client
    try:
        response = http_client.get(TARGET_URL)
        print(i, f"{(datetime.now() - start_time).microseconds / 1000}ms", response.status_code, response.text)
    except RemoteDisconnected as e:
        print(i, f"{(datetime.now() - start_time).microseconds / 1000}ms", "FAILED")
