import mariadb
#강사코드
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

sql = 'SELECT  * FROM `edu`.`NOTICE` WHERE id = 1'
cur.execute(sql)
result = cur.fetchone()

col_name = cur.description
name = ""
for row in col_name:
    name += row[0] + ("\t\t" if row[0] == 'created_at' else "\t")
print(name)

if result == None:
    print("데이터가 없습니다.")
else:
    행 = ""
    # print('no\ttitle\tdesc\tcontent\tregDate\t\t\tmodDate')
    for col in result:        
        if col == None:
            행 += "없다\t"
        else:
            행 += f'{col}\t'
    print(행)

cur.close()
conn.close()