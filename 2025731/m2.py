#7월 31일 오름차순,내림차순으로 정렬하고 값을 비교 하여 추출하는 예제
import pandas as pd

a1 = [60, 84, 80, 70, 19]
a2 = [77, 62, 95, 85, 17]
a3 = [61, 97, 72, 67, 15]
a4 = [75, 65, 95, 51, 18]

cols = ["국어", "영어", "수학", "과학", "나이"]
idx = ["A","B","C","D"]

data = pd.DataFrame([a1, a2, a3, a4], index=idx, columns=cols)

#print(data)
#print(data.sort_values('영어',ascending=False)) # 내림차순정렬

print(data.sort_values(by=['수학','영어'],ascending=[0,1]))
#Q1 위의 성적표에서 수학점수가 동률인 것만 출력하시오
d1 = data["수학"].sort_values(ascending=0)
cnt = d1.value_counts()
#print(d1 == cnt[cnt > 1 ].index[0])
print(d1[d1 == cnt[cnt > 1 ].index[0]])