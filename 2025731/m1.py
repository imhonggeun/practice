#7월 31일
# 열,행을 합치는 개념 
import pandas as pd

#print(pd.__version__)

arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    
]

idx = ['열1','열2','열3']
col = ['행1','행2','행3'] 
data1 = pd.DataFrame(arr,idx,col)
print(data1)

data2 = pd.DataFrame(arr[1:],idx[1:],col)
print(data1 + data2)


data3 = data1 + data2
s = pd.Series()
print(data3 + s)