import os
from flask import Flask, render_template, jsonify, request
import requests
from dotenv import load_dotenv
import yfinance as yf

from auth import get_access_token
from holding import get_my_holdings  # 보유 종목 조회 함수

load_dotenv()

app = Flask(__name__)

# 1. 메인 대시보드 화면 렌더링
@app.route('/')
def index():
    return render_template('index2.html')

# 2. 보유 종목 및 평가 데이터 조회 엔드포인트 (5초 폴링용)
@app.route('/api/dashboard-data')
def dashboard_data():
    try:
        # holding.py 내부의 계좌 보유 종목 조회 호출
        holdings_data = get_my_holdings()
        if holdings_data:
            return jsonify({
                "status": "success",
                "holdings": holdings_data
            })
        else:
            return jsonify({
                "status": "error",
                "message": "보유 종목 데이터를 불러올 수 없습니다."
            }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

# 3. 토스증권 일봉 캔들 조회 엔드포인트
@app.route('/api/candles')
def get_candles():
    symbol = request.args.get('symbol', 'QLD').upper().strip()
    try:
        ticker = yf.Ticker(symbol)
        # 전체 기간 일봉 조회
        df = ticker.history(period='max', interval='1d')
        
        if df.empty:
            return jsonify({"status": "error", "message": f"{symbol} 시세 데이터를 찾을 수 없습니다."}), 404

        candles = []
        for idx, row in df.iterrows():
            # 일봉 차트는 'YYYY-MM-DD' 형식의 문자열이 가장 안정적입니다.
            date_str = idx.strftime('%Y-%m-%d')
            candles.append({
                "time": date_str,
                "open": round(float(row['Open']), 2),
                "high": round(float(row['High']), 2),
                "low": round(float(row['Low']), 2),
                "close": round(float(row['Close']), 2)
            })

        return jsonify({"status": "success", "data": candles})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # 개발 서버 실행
    app.run(debug=True, port=5000)