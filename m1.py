import pandas as pd
import matplotlib.pyplot as plt

#한글 해결
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

#데이터 만들기
data = pd.read_csv('./data1_20220731.csv',index_col=0)

#선차트
#data.plot()

#막대 차트
#data.plot(kind='bar')

#히스토그램
#data.plot(kind='hist', y='세대수')

#산점도
#data.plot(kind='scatter', x='남',y='여')

#원형 그래프
#data.plot(kind='pie' ,y='세대수', autopct='%.1f%%')

data.plot('bo--')
plt.xlabel('X-axis')
plt.xlabel('Y-axis')
plt.show()

