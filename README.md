# AI 추천 서비스 영업 대시보드 (Streamlit)
AI 추천 서비스 영업 대시보드 (stream lit)
## 파일
- `app.py` : 대시보드 HTML을 화면 가득 띄우는 Streamlit 앱
- `dashboard.html` : 대시보드 (실제 상호·URL 포함, 데이터 3,864곳 내장)
- `dashboard_public.html` : 공개용 (상호를 "쇼핑몰 0001"로 바꾸고 도메인·URL 제거)
- `requirements.txt`, `.streamlit/config.toml`

공개용으로 바꾸려면 `app.py`의 `HTML_FILE = "dashboard.html"`을 `"dashboard_public.html"`로 바꾸세요.

## 내 컴퓨터에서 실행
```
pip install streamlit
streamlit run app.py
```

## 데이터
서울 독립 쇼핑몰 3,864곳 (2026년 10월 사이트 스캔, 공정위 통신판매사업자 등록 현황)
