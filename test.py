import streamlit as st
import pandas as pd

st.title("빙그레 해커톤 대시보드 🍦")

st.subheader("📝 데이터 직접 수정하기")

# 수정 가능한 데이터 입력
data = {
    "이름": ["김철수", "이영희", "박민준", "최수진", "정태양"],
    "부서": ["영업", "마케팅", "영업", "마케팅", "영업"],
    "매출": [1200, 850, 1500, 920, 1100]
}

df = pd.DataFrame(data)

# 수정 가능한 테이블
edited_df = st.data_editor(df)

st.subheader("💰 매출 평균")
st.metric("평균 매출", f"{edited_df['매출'].mean():.0f} 만원")

st.subheader("📊 부서별 매출")

# 가로 이름 표시 막대 그래프
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'Malgun Gothic'

fig, ax = plt.subplots()
ax.bar(edited_df["이름"], edited_df["매출"], color="steelblue")
ax.set_xlabel("이름")
ax.set_ylabel("매출 (만원)")
plt.xticks(rotation=0)

st.pyplot(fig)