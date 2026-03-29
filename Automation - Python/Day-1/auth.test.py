import requests


switch_ip = "192.168.99.30"
login_url = f"https://{switch_ip}/rest/v10.13/login"

Credentials = {
    "username": "admin",
    "password": "Admin@eve"
}

print(f"Attempting to log into Switch-1 at {switch_ip}...")

try:
    response = requests.post(login_url, data=Credentials, verify=False, timeout=5)
    
    if response.status_code == 200:
        print("✅ Success! You are Logged-in.")
        print(f"Session Cookie Received: {response.cookies.get_dict()}")
    else:
        print("❌ Failed to Login")
        print(response.text)

except Exception as e:
    print(f"🚨 Connection Failed: {e}")