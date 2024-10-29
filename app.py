import streamlit as st
import altair as alt
import pandas as pd

# 페이지 제목
st.set_page_config(
    page_title="경제금융교육연구회",         # 페이지 제목
    page_icon="image/pre.png",        # 파비콘 파일 경로 (예: image 폴더 안에 favicon.ico)
    layout="wide"                         # 레이아웃 설정
)

st.title("경제금융교육연구회")

# CSS 스타일 추가
st.markdown("""
    <style>
        /* 버튼 스타일 */
        .button-container {
            display: flex;
            justify-content: space-around;
            margin-top: 20px;
            margin-bottom: 40px;
        }
        
        .button-link {
            background-color: #4c6ef5;
            color: white !important;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 1.1rem;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            width: 100%;
        }

        .button-link:hover {
            background-color: #3b5cc6;
            color: #f1f1f1 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3개의 열 생성
col1, col2, col3 = st.columns(3)

# 버튼 1: 강좌신청 확인 (현재 탭에서 열림)
with col1:
    st.markdown(
        '<a class="button-link" href="https://241109.streamlit.app/roll" target="_self">강좌신청 확인하기🔍</a>',
        unsafe_allow_html=True
    )

# 버튼 2: 오픈채팅방 (새 탭에서 열림)
with col2:
    st.markdown(
        '<a class="button-link" href="https://open.kakao.com/o/g141aCVg" target="_blank">오픈채팅방 입장👨🏻‍💻</a>',
        unsafe_allow_html=True
    )

# 버튼 3: 연수후기 (새 탭에서 열림)
with col3:
    st.markdown(
        '<a class="button-link" href="https://bit.ly/econo1109" target="_blank">연수후기 남기기🖼</a>',
        unsafe_allow_html=True
    )

# 오프연수회 일시 및 장소 섹션
st.header("📅 오프연수회 일시 및 장소")
st.markdown("""
✅ **일시**: 2024. 11. 9. (토) 10:30~17:40  
*(끝나고 희망자에 한해 뒤풀이도 있어요!!!🍺)*

✅ **장소**: 전국투자자교육협의회 6, 7층  
(서울 영등포구 여의나루로 67-8)  
지하철 이용 시: 여의도역(5, 9호선) 4번 출구 이용
""")
st.image("image/map.png", caption="", use_column_width=True)

st.markdown("""
✅ **점심 식사**  
참가 확정 후 희망하는 분에 한해 도시락 및 근처 식당 예약을 받을 예정입니다.

✅ **준비물**  
필기도구를 준비해주세요. 몇몇 강의는 별도의 강의안을 인쇄하여 제공할 예정입니다.  
전체 교안과 PPT는 따로 제공되지 않습니다.
""")

st.image("image/1.jpg", caption="연수안내", use_column_width=True)
st.image("image/2.png", caption="연수안내", use_column_width=True)
