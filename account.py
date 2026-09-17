# account.py
import requests
from auth import get_access_token

BASE_URL = "https://openapi.tossinvest.com"

def get_my_accounts():
    token = get_access_token()
    if not token:
        print("[account.py] 토큰 발급 실패")
        return None

    url = f"{BASE_URL}/api/v1/accounts"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()  # 정상 데이터 반환
        else:
            print(f"[account.py 조회 실패] {response.status_code}: {response.text}")
            return None
    except Exception as e:
        print(f"[account.py 예외]: {e}")
        return None

if __name__ == "__main__":
    print(get_my_accounts())