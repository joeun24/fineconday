import streamlit as st
import altair as alt
import pandas as pd

map_html = """
<iframe 
    src="https://naver.me/FGoFaelR"
    width="700" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade">
</iframe>
"""


# 페이지 제목
st.title("경제금융교육연구회")

# 오프연수회 일시 및 장소 섹션
st.header("📅 오프연수회 일시 및 장소")
st.markdown("""
✅ **일시**: 2024. 11. 9. (토) 10:30~17:40  
*(끝나고 희망자에 한해 뒤풀이도 있어요!!!🍺)*

✅ **장소**: 전국투자자교육협의회 6, 7층  
(서울 영등포구 여의나루로 67-8)  
지하철 이용 시: 여의도역(5, 9호선) 4번 출구 이용
""")


# HTML로 Google Maps 표시
st.components.v1.html(map_html, height=500)


st.markdown("""
✅ **점심 식사**  
참가 확정 후 희망하는 분에 한해 도시락 및 근처 식당 예약을 받을 예정입니다.

✅ **준비물**  
필기도구를 준비해주세요. 몇몇 강의는 별도의 강의안을 인쇄하여 제공할 예정입니다.  
전체 교안과 PPT는 따로 제공되지 않습니다.
""")

image_path = "image/1.jpg"
st.image(image_path, caption="연수안내", use_column_width=True)

