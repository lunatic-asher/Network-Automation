import requests 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

login_url = f"https://{192.168.99.30}/rest/v10.13/login"

Credentials = {
    "username": admin,
    "password": Admin@eve
}

print(f"Attempting to log into Switch-1 at {192.168.99.30}")

try: 
    respone = requests.post(login_url, data=Credentials, verify=False, timeout=5)

    if respone.static_code == 200: 
        print("Sucess! You are Logged-in.")
        print(f"Session Cookie Received: {respone.cookies.get_dict()}")
    else:
        print("Failed to Login")
        print(respone.text)

except Exception as e:
    print(f"Connection Failed: {e}")
    