import requests
import csv

ip = open( "D:\\sankar\\intern task\\ip.txt", "r")
ips = []
ip_city_data = []
header = ["ip", "city"]
while 'true':
    data = ip.readline()
    ips.append(data.strip())
    if not data :
       break
ip.close()

for ip in ips:
    if ip:
        response = requests.get(f"http://ipinfo.io/{ip}/geo")
        if response.status_code == 200:
            data = response.json()
            city = data.get("city", "Unknown city")
            ip_city_data.append((ip, city))
    else:
        break        
    
    
with open("ip_city.csv","w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(ip_city_data)
    
    
    
    
    
   