import requests
domain = "https://www.weareplymouths.com/"
headers = requests.get(domain).headers
print headers

if 'X-Frame-Options' in headers :
    print domain + " is SAFE"
else:
    print domain + " is VULNERABLE"
