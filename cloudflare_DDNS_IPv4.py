
"""

By ArenAvak

for support and donnations 
tron_Address : TFXSXuRAkNRNEKtWCNSXKjTWQQ2kTQy2Yu


"""
import requests


zone_identifier= ""            #zone id , you can find it on overviw of your domain in cloudflare
record_name=     ''            # subdomain example : subdomain.example.com
X_Auth_Email=    ""            # your email that you signed up in cloudflare
X_Auth_Key=      ""            # on overviw page of cloudflare right down of the Account id , press 'get api token' and then 'create token '
Commentt=        ""






def create(ip,zone_identifier,X_Auth_Email,X_Auth_Key,record_name,commentt):

    
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"

    payload = {
    "content": f"{ip}",
    "name": f"{record_name}",
    "proxied": False,
    "type": "A",
    "comment": f"{commentt}",
    "ttl": 3600
}
    headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": f"{X_Auth_Email}",
    "X-Auth-Key"    : f"{X_Auth_Key}"

}

    response = requests.request("POST", url, json=payload, headers=headers)

    print("created")


def update(ip,zone_identifier,X_Auth_Email,X_Auth_Key,record_name,record_id,commentt):
    url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records/{record_id}"

    payload = {
    "content": f"{ip}",
    "name": f"{record_name}",
    "proxied": False,
    "type": "A",
    "comment": f"{commentt}",
    "ttl": 3600
    }
    headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": f"{X_Auth_Email}",
    "X-Auth-Key"    : f"{X_Auth_Key}"
    }

    response = requests.request("PUT", url, json=payload, headers=headers)

    print("Updated")

#scan ip address and location 
url = "https://cloudflare.com/cdn-cgi/trace"
response = requests.get(url)
if response.status_code == 200:
    response = requests.get(url)
    response=response.text
    response=response.split("\n")
    ip= response[2]
    ip=ip[3::]
    loc=response[9]
    loc=loc[4::]
    
    print(f"IP Address = {ip}\nIP Location = {loc}")
else:
    print("cannot scan your ip adddres ")



#scan
url = f"https://api.cloudflare.com/client/v4/zones/{zone_identifier}/dns_records"
text='{"id":'
List=[]
flag=False

headers = {
    "Content-Type": "application/json",
    "X-Auth-Email": f"{X_Auth_Email}",
    "X-Auth-Key"    : f"{X_Auth_Key}"
}

response = requests.request("GET", url, headers=headers)
response=response.text
response=response[10::]
response=response[:-127]
response=response.split(text)
response.pop(0)
for i in response :
    records=[]
    i=i.split('"')
    record=i[13]
    zone_id=i[1]
    records.append(record)
    records.append(zone_id)
    List.append(records)


for i in List :
    if record_name==i[0]:
        flag=True
        record_id=i[1]
        print(i[0])

#print(record_id)


if flag==False:
    create(ip,zone_identifier,X_Auth_Email,X_Auth_Key,record_name,Commentt)
else:
    update(ip,zone_identifier,X_Auth_Email,X_Auth_Key,record_name,record_id,Commentt)


































