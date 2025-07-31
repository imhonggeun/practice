import pandas as pd

data = pd.read_csv('./data1_20220731.csv')


# Q2 위의 인구수 표에서 '세대수'가 가장 높은 동명은 무엇인가요?

#sort_vales 정렬하는 함수 
#(by=['세대수'],ascending=[0]) 어떤 컬럼으로 정렬할건지 지정해주고 ascending 으로 내림차순,올림차순을 정하는하고 0(false , 1 true 로 되며 0내림차순,1올림차순이다)
Q2 = data.sort_values(by=['세대수'],ascending=[0])
#print(Q2)

#iloc => 인덱스 값으로 찾기 :iloc[0] 첫번째 인덱스 값만 출력(한줄)
#loc => 정확한 이름으로 값을 찾기 :loc["동명"] 지정명으로 찾는것
print(Q2.iloc[0].loc["동명"])

# Q3 위의 인구수 표에서 '남(65세 이상)' 인구수가 높은 동명은 무엇인가요?

#sort_values는 정렬 메서드
#(by=['남(65세이상)'],ascending=[0]) 어떤 컬럼으로 정렬할건지 지정해주고 ascending 으로 내림차순,올림차순을 정하는하고 0(false , 1 true 로 되며 0내림차순,1올림차순이다)
Q3 = data.sort_values(by=['남(65세이상)'],ascending=[0])
#print(Q3)
print(Q3.iloc[0].loc["동명"])



# Q4 위의 인구수 표에서 '세대수'의 평균 이상 인구수의 동명은 무엇인가요? 
#평균값 구하는 코드..공부
평균값 = data['세대수'].mean().astype(int)
#data에 있는 세대수 컬럼 이랑 평균값 세대수컬럼이랑 비교 해서 전체 데이터 값을 구함
Q4 = data[data['세대수'] > 평균값]
#print(Q4)
#전체 데이터에서 컬럼 값 전체를 찾아서 출력
print(Q4["동명"])


#동근
#평균값=data['세대수'].mean().astype(int)
#print(평균값)
#print(data['세대수']>=평균값)
#print(data[data['세대수']>=평균값])
#print(data[data['세대수']>=평균값].index)
