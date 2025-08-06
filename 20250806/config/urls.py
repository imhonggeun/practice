def get():
    return {"test" : "읽기"}
def post():
    return {"test" : "post 수정"}
def put():
    return {"test" : "put 입력"}
def delete():
    return {"test" : "delete 삭제"}

ctr1 = [
  {
    "methods":["GET"],"path":"/", "summary":"기본 조회", "description":"기본 정보를 조회합니다.","endpoint": get
  },
  {
    "methods":["POST"],"path":"/", "summary":"데이터 수정", "description":"데이터를 수정합니다.","endpoint": post
  },
  {
    "methods":["PUT"],"path":"/", "summary":"데이터 입력", "description":"새로운 데이터를 입력합니다.","endpoint": put
  },
  {
    "methods":["DELETE"],"path":"/", "summary":"데이터 삭제", "description":"데이터를 삭제합니다.","endpoint": delete
  }
]
ctr2 = {
  "get": {
    "path":"/", "summary":"기본 조회", "description":"기본 정보를 조회합니다."
  },
  "post": {
    "path":"/", "summary":"데이터 수정", "description":"데이터를 수정합니다."
  },
  "put": {
    "path":"/", "summary":"데이터 입력", "description":"새로운 데이터를 입력합니다."
  },
  "delete": {
    "path":"/", "summary":"데이터 삭제", "description":"데이터를 삭제합니다."
  }
}

urls = [ctr1, ctr2]