import pandas as pd

data = pd.read_csv('./data1_20220731.csv')


# Q2 위의 인구수 표에서 '세대수'가 가장 높은 동명은 무엇인가요?
d1 = data.sort_values(by=['세대수'],ascending=[0])
print(d1)
#print(d1.iloc[0].loc["동명"])

# Q3 위의 인구수 표에서 '남(65세 이상)' 인구수가 높은 동명은 
# 무엇인가요?
#d1 = data.sort_values(by=['남(65세이상)'],ascending=[0])
#print(d1)
#print(d1.iloc[0])
#print(d1.iloc[0].loc["동명"])

# Q4 위의 인구수 표에서 '세대수'의 평균 이상 인구수의 동명은 무엇인가요? 
#평균값 = data['세대수'].mean().astype(int)
#data = data[data['세대수'] > 평균값]
#print(data)
#print(data["동명"])


#동근
#평균값=data['세대수'].mean().astype(int)
#print(평균값)
#print(data['세대수']>=평균값)
#print(data[data['세대수']>=평균값])
#print(data[data['세대수']>=평균값].index)
