import mariadb

def mradb():
    conn_params= {
        "user" : "study",
        "password" : "study",
        "host" : "localhost",
        "database" : "edu",
        "port" : 3306
    }
    return mariadb.connect(**conn_params)

def read():
    conn = mradb()
    cur= conn.cursor()
    ## 생성
    sql ='SELECT * FROM notice;'

    cur.execute(sql)
    result = cur.fetchall()


    col_name = cur.description # 각컬럼에 대한 정보를 담은 튜플들의 리스트
    #print(result) #print(type(result)) /
    #print(col_name) #print(type(col_name))


    # x축 컬럼명
    # name = ''
    # for row in col_name:
    #     name += row[0]
    #print(name)

    # 데이터 가져오기 -> 왜리스트로 나오지?
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
        return row #리턴 값이 없어서 하루종일 밑에 read() none 나옴
    #print(f'결과값 :{result}')
    cur.close()
    conn.close()

def Create():
    conn = mradb()
    cur= conn.cursor()
    ## 생성
    title = input("제목을 입력하세요")
    content = input("내용을 입력하세요")
    author = input("이름을 입력하세요")
    sql =f"INSERT INTO notice (`title`, `content`,`author`) VALUES ('{title}','{content}','{author}');"

    cur.execute(sql)
    conn.commit()
    
    cur.close()
    conn.close
    #?? 리턴값이 없어도 되나? -> cur 아니고 conn객체에서 commit 가능

def read_chose():
    conn = mradb()
    cur= conn.cursor()
    id = int(input('숫자를 입력하세요'))
    sql = f'select * from notice where id = {id};'
    
    cur.execute(sql)
    result = cur.fetchone()
    
    if result == None:
        print('해당 번호는 데이터가 삭제되거나 없습니다.')
    else :
        list =''
        for row in result:
            list += f'{row}\t'
        #print(f'read_chose 너야 ?{list}')
        return list
    
    cur.close()
    conn.close()

def modify(): # None
    conn = mradb()
    cur= conn.cursor()
    id = input("수정할 번호을 입력하세요")
    title = input("수정할 제목을 입력하세요")
    content = input("수정할 내용을 입력하세요")
    author = input("수정할 이름을 입력하세요")
    
    txt = '' #값을 받기위해서 생성
    #제목
    if title != '':
        txt = f"title ='{title}'" #여기는 없는데 -> 처음이라 없어도 됨 & '{title}' 아니고 `{title}`일때 출력이 됨 뭘까?
    #내용작성
    if content !='':
        #txt += f",'`content'='{content}' " # 앞에 ,를 받아야되서 ``필요함 -> +로 표현가능한가?
        txt +="," + f"content ='{content}'" #if txt !='' else f"content ='{content}'" #값이 그대로 라서 ``이게 없어도 됨 
        if txt !='':
            txt
        else :
            f"content = '{content}' "
    
    if author !='':
        #txt += f", `author' = '{author}'"
        txt +="," + f"content ='{author}'" #if txt !='' else  f"author='{author}'"
        if txt !='' :
            txt
        else:  
            f"author = '{author}'"
    if txt !='':
        sql =f"UPDATE notice SET {txt} WHERE id={id};"
            
    #sql =f"UPDATE notice SET `title`='{title}', `content`='{content}', `author`='{author}' WHERE id={id};"
    
    cur.execute(sql)
    result = conn.commit()  #insert,updat,delete fetch X, commit O -> commit 같은 경우 conn으로 사용

    #return result # none 이 왜나오지?! -> commit 이라서 return이 필요 없다?

def delete(): #None
    conn = mradb()
    cur= conn.cursor()
    id = int(input('숫자를 입력하세요'))
    
    sql = f'DELETE FROM notice WHERE  id={id};'
    cur.execute(sql)
    conn.commit()
    
    cur.close()
    conn.close()
    
#print(f'너야?{read()}')

while True :
    CRUD = input("CRUD중에 입력하세요")
    if CRUD == 'c':
        print(Create())
    elif CRUD == 'r' :
        list = input('a 또는 c을 입력해주세요.') 
        if list == 'a':
            print(read())
        elif list == 'c':
            print(read_chose())
    elif CRUD == 'u':
        print(modify())
    elif CRUD == 'd':
        print(delete())
    else:
        print('잘못 입력하셨습니다.다시 실행해주세요')
        break