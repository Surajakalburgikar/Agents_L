import requests

response = requests.get("https://api.github.com")
data = response.json()

print("Status:", response.status_code)
print("API Message:", data.get("current_user_url"))
