from http.client import RemoteDisconnected
import requests
from datetime import datetime
import hashlib

TARGET_URL = "https://api-0.752628.xyz/dummy/auth/decrypt"
MY_TOKEN = "12345678"

for i in range(100000):
    try:
        start_time = datetime.now()
        response = requests.get(f"https://api-0.752628.xyz/dummy/auth/decrypt?encrypted_string={hashlib.sha512((MY_TOKEN+str(int(start_time.timestamp()))).encode('utf-8')).hexdigest()}&auth_token={MY_TOKEN}&timestamp={int(start_time.timestamp())}")
        print(i, str(datetime.now() - start_time), response.status_code, response.text)
    except RemoteDisconnected as e:
        print(i, str(datetime.now() - start_time), "FAILED")