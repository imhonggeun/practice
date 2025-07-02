import mariadb
import os

def 마리아디비():
    conn_params = {
        "user" : os.getenv('MARIADB_USER'),
        "password" : os.getenv('MARIADB_PASSWORD'),
        "host" : os.getenv('MARIADB_HOST'),
        "database" : os.getenv('MARIADB_DATABASE'),
        "port" : int(os.getenv('MARIADB_PORT'))
    }
    return mariadb.connect(**conn_params)

## 생성

def 입력(): 
    conn = 마리아디비()
    cur = conn.cursor()

    title = input("제목을 입력하세요.")
    desc = input("설명을 입력하세요.")

    sql = f"INSERT INTO NOTICE (`title`, `desc`) VALUE ('{title}', '{desc}')"
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

def 읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    
    sql = 'SELECT  * FROM `edu`.`NOTICE` WHERE delYn = false'
    cur.execute(sql)
    result = cur.fetchall()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        for row in result:
            행 = ""
            for col in row:
                if col == None:
                    행 += "\t"
                else:
                    행 += f'{col} '
            print(행)
    
    cur.close()
    conn.close()
    
def 선택적읽기():
    conn = 마리아디비()
    cur = conn.cursor()
    
    no = input("NO 컬럼의 값을 입력해주세요.")
    
    sql = f'SELECT  * FROM `edu`.`NOTICE` WHERE delYn = false AND no = {no}'
    cur.execute(sql)
    result = cur.fetchone()
    
    if result == None:
        print("데이터가 없습니다.")
    else:
        행 = ""
        for col in result:
            if col == None:
                행 += "\t"
            else:
                행 += f'{col} '
        print(행)
    
    cur.close()
    conn.close()

def 삭제(): 
    conn = 마리아디비()
    cur = conn.cursor()

    no = input("NO 컬럼의 값을 입력해주세요.")

    # sql = f"DELETE FROM NOTICE WHERE no = {no}"
    sql = f"UPDATE NOTICE SET delYn = true WHERE no = {no}"
    cur.execute(sql)
    conn.commit()

    cur.close()
    conn.close()

def 수정():
    conn = 마리아디비()
    cur = conn.cursor()

    no = input("NO 컬럼의 값을 입력해주세요.")
    title = input("제목을 입력하세요.")
    desc = input("설명을 입력하세요.")
    content = input("내용을 입력하세요.")
    
    txt = ""
    if title != "":
       txt += f"title='{title}'"
    if desc != "":
        txt += f", `desc`='{desc}'" if txt != "" else f"`desc`='{desc}'"
    if content != "":
        txt += f", content = '{content}'" if txt != "" else f"content = '{content}'"

    if txt != "":
        sql = f"UPDATE NOTICE SET {txt} WHERE  no = {no}"
        cur.execute(sql)
        conn.commit()

    cur.close()
    conn.close()

while True:
    모드 = input("CRUD 중 선택하세요.")
    print("="*100)
    if 모드 == 'C':
        입력()
    elif 모드 == 'R':
        타입 = input("전체 또는 선택적으로 가져올까요?")
        if 타입 == "전체":
            읽기()
        elif 타입 == "선택적":
            선택적읽기()
    elif 모드 == "U":
        수정()
    elif 모드 == "D":
        삭제()
    else:
        break
    print("="*100)