<img width="845" height="866" alt="image" src="https://github.com/user-attachments/assets/2b25c407-c43c-42e1-8799-a055c2265f80" />
# 📈 주식 포트폴리오 & 일봉 차트 대시보드 (Stock Portfolio Dashboard)

토스증권 OpenAPI와 Yahoo Finance를 연동하여 실시간 보유 자산 현황과 종목별 전체 일봉 차트를 시각화하는 웹 대시보드입니다.

---

## 🚀 주요 기능
* **포트폴리오 실시간 모니터링**: 토스증권 계좌의 보유 종목, 매입단가, 평가손익, 수익률 5초 단위 자동 갱신
* **전체 일봉 차트 시각화**: `yfinance` 기반 상장 이래 전 기간 일봉 캔들스틱 차트 제공 (Lightweight Charts 연동)
* **인터랙티브 종목 전환**: 보유 목록 클릭 또는 상단 티커 검색을 통한 즉각적인 차트 로드 및 화면 크기 자동 맞춤

---

## 🛠 기술 스택
* **Backend**: Python 3.x, Flask, Requests, yfinance, python-dotenv
* **Frontend**: HTML5/CSS3, JavaScript (Vanilla), TradingView Lightweight Charts (v4.1.1)
* **Data Sources**: 토스증권 OpenAPI (보유자산), Yahoo Finance (일봉 시세)

---

## ⚙️ 실행 방법

### 1. 저장소 클론 및 이동
\`\`\`bash
git clone https://github.com/chohyoungjun02/stock_portfolio.git
cd stock_portfolio
\`\`\`

### 2. 가상환경 구성 및 패키지 설치
\`\`\`bash
python -m venv .venv
source .venv/Scripts/activate  # Windows PowerShell/Bash 기준
pip install flask requests yfinance python-dotenv
\`\`\`

### 3. 환경 변수 설정 (`.env`)
프로젝트 루트 디렉터리에 `.env` 파일을 생성하고 인증 키를 입력합니다.
\`\`\`env
TOSS_API_KEY=your_api_key_here
TOSS_SECRET_KEY=your_secret_key_here
\`\`\`
> **주의**: `.env` 파일은 보안상 GitHub에 업로드되지 않으므로 로컬에서 직접 생성해야 합니다.

### 4. 서버 구동
\`\`\`bash
python app.py
\`\`\`
브라우저에서 `http://127.0.0.1:5000`으로 접속합니다.

---

## 📁 디렉터리 구조
\`\`\`text
├── templates/
│   └── index2.html       # 대시보드 및 차트 UI
├── app.py                # Flask 서버 라우팅 및 API 엔드포인트
├── auth.py               # 토스증권 인증 토큰 발급
├── holding.py            # 계좌 보유 주식 조회
├── .gitignore            # Git 제외 설정 (.env, venv 등)
└── README.md             # 프로젝트 안내 문서
\`\`\`
