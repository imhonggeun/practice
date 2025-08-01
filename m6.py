import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# 선택 년도 기본값
if 'slider_value' not in st.session_state:
  st.session_state.slider_value = (2019,2023)
# 차트 기본값
if 'chart_value' not in st.session_state:
  st.session_state.chart_value = pd.DataFrame([])

# 데이터 1차 전처리
url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
data = pd.read_html(url)
df = data[0].drop(0)
df = df.drop("Unnamed: 1", axis=1)
data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# st.dataframe(data1)

#함수로 변경
def getItems():
 # 선택한 데이터 전처리
  st.text(f"선택한 년도 {st.session_state.slider_value}")
  ty = st.session_state.slider_value
  arr = []
  for y in range(ty[0], ty[1] + 1):
    arr.append(str(y))
  return arr

def makeData():
  # st.dataframe(data1)
 
  st.session_state.chart_value = data1.filter(items=getItems()).transpose()
  st.dataframe(st.session_state.chart_value)
  st.bar_chart(st.session_state.chart_value)

# 선택 하는 슬라이더 추가
sd = st.slider(label="년도 범위를 변경하세요.", min_value=1989, max_value=2023, value=st.session_state.slider_value, step=1)  
if st.button("선택한 범위 확인"):
  st.session_state.slider_value = sd
  # st.text(f"변경한 년도 {st.session_state.slider_value}")
  makeData()