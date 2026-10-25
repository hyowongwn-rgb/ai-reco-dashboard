from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI 추천 서비스 영업 대시보드", page_icon="📊", layout="wide")

# Streamlit 기본 여백·헤더·푸터 숨기기 (대시보드만 꽉 차게)
st.markdown(
    """
    <style>
      #MainMenu, header, footer {visibility: hidden;}
      .block-container {padding: 0 !important; max-width: 100% !important;}
      [data-testid="stAppViewContainer"] {background: #faf9f5;}
    </style>
    """,
    unsafe_allow_html=True,
)

# 공개용(상호·URL 가림)으로 바꾸려면 "dashboard_public.html"로 바꾸면 된다
HTML_FILE = "dashboard_public.html"

html = (Path(__file__).parent / HTML_FILE).read_text(encoding="utf-8")
components.html(html, height=1600, scrolling=True)
