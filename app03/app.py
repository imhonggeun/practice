import mariadb

conn_params= {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu",
    "port" : 3306
}

## 생성

conn= mariadb.connect(**conn_params)
cur= conn.cursor()

sql ='SELECT * FROM notice where id = 1;'

cur.execute(sql)
result = cur.fetchone()


col_name = cur.description # 각컬럼에 대한 정보를 담은 튜플들의 리스트
#print(result) #print(type(result)) /
#print(col_name) #print(type(col_name))


# x축 컬럼명
# name = ''
# for row in col_name:
#     name += row[0]
#print(name)

# 데이터 가져오기
if result == None :
    print('데이터가 없습니다.')
else:
    row=''
    for col in result:
        if col == 'none':
            row +=('없음\t')
        else:
            row +=(f'{col}\t')
        #print(f'result: {result}')
        #print(f'col : {col}')
    print(f'로우 : {row}')
#print(f'결과값 :{result}')



cur.close()
conn.close()