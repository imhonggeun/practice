#이벤트 버튼 활용법
import streamlit as st
import pandas as pd

btn = st.button("버튼")

if btn:
    st.write(":blue[버튼] 으악!!")
    
#CSV 데이터 원본
df =pd.DataFrame({
    "첫번째" : [1,2,3,4],
    "두번째" : [5,6,7,8]
})

#파일 다운로드 버튼 이벤트
st.download_button(
    label = "CSV 다운로드",
    data = df.to_csv(),
    file_name="샘플.csv",
    mime="text/csv"
)


#요청 버튼 이벤트
with st.form(key="me"):
    id = st.text_input("아이디를 입력하세요")
    stbn = st.form_submit_button("호출")

if stbn:
    st.success(f"확인 : {id}")
    
  
  
  
    
#선택 이벤트
r = st.radio(
    label = "식사하셨어요?",
    options = ("먹었다","안먹었다","생각중"),
    #index=1
)
if r=="먹었다":
    st.text("배불러!!")
elif r=="안먹었다":
    st.text("배고파!")
else:
    st.text("중식 한식 양식")
    
    
    
#선택 이벤트2 select
select = st.selectbox(
    label = "식사하셨어요?",
    options = ("먹었다","안먹었다","생각중"),
    #index=0
)
if select=="먹었다":
    st.write("배불러!!")
elif select=="안먹었다":
   st.write("배고파!")
else:
    st.write("중식 한식 양식")
    
    
    
   
#선택 이벤트3 multiselect 
multi = st.multiselect(
    "종아하는 것은 무엇인가요?",
    ["#사과", "#배" ,"#망고"],
    ["#사과"]
)
st.write(f"당신의 선택은: :green[{multi}] 입니다.")





#선택 이벤트 slider
from datetime import datetime as dt
import datetime

점심 = st.slider(
    "점심 시간은 언제 좋을까요?",
    min_value=dt(2024, 12, 5, 13, 20),
    max_value=dt(2024, 12, 5, 14, 30),
    value=dt(2024, 12, 5, 13, 30),
    step=datetime.timedelta(minutes=10),
    format="MM/DD/YY HH:mm"
)
st.write("선택한 시간:", 점심)