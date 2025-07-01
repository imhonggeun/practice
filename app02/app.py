import mariadb

# connection parameters
conn_params= {
    "user" : "study",
    "password" : "study",
    "host" : "localhost",
    "database" : "edu"
}

# Establish a connection
# conn = connection cur = cursor
conn= mariadb.connect(**conn_params) # **가 있을 때 딕셔너리의 키-값을 쌍을 풀어서 함수에 넣거나 함수의정의해준다
# connect 으로 연결까지 다하고 실행을 해서 문제가 없으면 성공


cur= conn.cursor()
sql = 'SELECT * FROM NOTICE WHERE no = 1'
# Populate countries table  with some data
cur.execute(sql) # 실행
result = cur.fetchone()
if result == 'none':
    print("데이터없습니다.")
else :
    row =''
    for col in result:
        print(col)
        row += f'{col} \t'
    print(row)

cur.close()
conn.close()

