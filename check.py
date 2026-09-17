import requests
from auth import get_access_token

token = get_access_token()
url = "https://openapi.tossinvest.com/api/v1/accounts"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

res = requests.get(url, headers=headers)
print("상태 코드:", res.status_code)
print("내 계좌 전체 응답:", res.text)