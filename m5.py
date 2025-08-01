import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
data = pd.read_html(url)
df = data[0].drop(0)
df = df.drop("Unnamed: 1", axis=1)
# print(df)
data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# print(data1)
data2 = data1.filter(items=["2023"]).transpose()
st.dataframe(data1)


#선택 년도 기본값
if 'slider_value' not in st.session_state:
    st.session_state.slider_value = (2018,2023)
if 'slider_value' not in st.session_state:
    st.session_state.chart_value = pd.DataFrame([])
#선택 하는 슬라이더 추가
st.slider(label="년도 범위를 입력하세요.",min_value=1989,max_value=2023,value=st.session_state.slider_value, step=1)

# 선택한 데이터 전처리
data2 = data1.filter(items=st.session_state.slider_value).transpose()
st.dataframe(data2)























# fig, ax = plt.subplots()
# ax.pie(data2.squeeze(), labels=data2.squeeze().index, autopct='%1.1f%%', startangle=90)
# ax.axis('equal')
# st.pyplot(fig)