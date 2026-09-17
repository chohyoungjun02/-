import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()  # .env 파일에서 환경 변수 로드

CLIENT_ID = os.getenv("TOSS_CLIENT_ID")
CLIENT_SECRET = os.getenv("TOSS_CLIENT_SECRET")

# 메모리에 토큰과 만료 시각을 저장하는 전역 변수
_cached_token = None
_token_expires_at = 0.0

def get_access_token() -> str:
    global _cached_token, _token_expires_at

    if not CLIENT_ID or not CLIENT_SECRET:
        print("[오류] CLIENT_ID 또는 CLIENT_SECRET이 설정되지 않았습니다. .env 파일을 확인하세요.")
        return None

    current_time = time.time()

    # 1. 이미 발급된 토큰이 있고, 만료까지 60초 이상 남아있다면 재사용
    if _cached_token and current_time < (_token_expires_at - 60):
        return _cached_token

    # 2. 토큰이 없거나 만료 직전일 때만 토스 서버로 신규 발급 요청
    url = "https://openapi.tossinvest.com/oauth2/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    print("\n[auth.py] 토큰 신규 발급/갱신 요청 중...")
    try:
        response = requests.post(url, headers=headers, data=data)
        
        if response.status_code == 200:
            token_data = response.json()
            _cached_token = token_data.get("access_token")
            
            # 토스에서 내려준 유효 기간(초 단위, 보통 86400초) 기준으로 만료 시점 계산
            expires_in = token_data.get("expires_in", 86400)
            _token_expires_at = current_time + expires_in
            
            print(f"[auth.py] 토큰 발급 성공 (유효 기간: {expires_in}초)")
            return _cached_token
        else:
            print(f"\n[auth.py 실패] 오류 응답 ({response.status_code}): {response.text}")
            return None
    except Exception as e:
        print(f"[auth.py 예외 발생]: {e}")
        return None

if __name__ == "__main__":
    t1 = get_access_token()
    if t1:
        print(f"첫 번째 호출 결과: {t1[:15]}...")
    
    t2 = get_access_token()
    if t2:
        print(f"두 번째 호출 결과 (캐시): {t2[:15]}...")