import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://www.index.go.kr/unity/potal/eNara/sub/showStblGams3.do?stts_cd=277002&idx_cd=2770&freq=Y&period=N'
data = pd.read_html(url)
df = data[0].drop(0)
df = df.drop("Unnamed: 1", axis=1)
# print(df)
data1 = df.iloc[::2, :].set_index(keys="Unnamed: 0")
# print(data1)
data2 = data1.filter(items=["2021","2022","2023"]).transpose()


#st.dataframe(data2)

#st.bar_chart(data2)
#st.line_chart(data2)
#선차트
# data2.plot()
# st.pyplot(data2)
# plt.show()

fig, ax = plt.subplots()
ax.pie(data2.squeeze(),labels=data.squeeze().index, autopct='%1.1f%%')
st.pyplot(fig)