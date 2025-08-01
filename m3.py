import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N

# arr =[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

st.title("테이블 화면")

#한글 해결
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

data = pd.read_csv("./data1_20220731.csv",index_col=0)

#st.dataframe(data)
#st.table(data) 

# 파이 차트를 그리기 위한 figure, axis 객체 생성
fig, ax = plt.subplots()

#'세대수'열을 기준으로 파이차트 그리기
# -labels : 인덱스를 라벨로 사용 (data,index)
# -autopct : 퍼센트 표시 형식 ('%1.1f%%')
ax.pie(data['세대수'],labels=data.index, autopct='%1.1f%%')

#원형 차트가 찌그러지지 않도록 축 비융르 동일하게 설정 옵션
#ax.axis('equal')

#완성된 차트 출력
st.pyplot(fig)