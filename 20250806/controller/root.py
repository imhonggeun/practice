from fastapi import APIRouter
from config.urls import urls

ctr1 = APIRouter()
for index in range(len(urls[0])):
    ctr1.add_api_route(**urls[0][index])
# ctr1.add_api_route(**urls[0][0])
# ctr1.add_api_route(**urls[0][1])
# ctr1.add_api_route(**urls[0][2])
# ctr1.add_api_route(**urls[0][3])

# @ctr1.get(**urls[0]["get"])
# def root():
#     return {"test" : "get 읽기"}
# @ctr1.post(**urls[0]["post"])
# def root():
#     return {"test" : "post 수정"}
# @ctr1.put(**urls[0]["put"])
# def root():
#     return {"test" : "put 입력"}
# @ctr1.delete(**urls[0]["delete"])
# def root():
#     return {"test" : "delete 삭제"}

ctr2 = APIRouter()
@ctr1.get(**urls[1]["get"])
def root():
    return {"test" : "get 읽기"}
@ctr1.post(**urls[1]["post"])
def root():
    return {"test" : "post 수정"}
@ctr1.put(**urls[1]["put"])
def root():
    return {"test" : "put 입력"}
@ctr1.delete(**urls[1]["delete"])
def root():
    return {"test" : "delete 삭제"}
######################################
# ctr1 = APIRouter(prefix="/ctr1")
# @ctr1.get("/")
# def root():
#     return {"test" : "get 읽기"}
# @ctr1.post("/")
# def root():
#     return {"test" : "post 수정"}
# @ctr1.put("/")
# def root():
#     return {"test" : "put 입력"}
# @ctr1.delete("/")
# def root():
#     return {"test" : "delete 삭제"}
######################################
# ctrl1 = APIRouter()
# @ctrl1.get("/")
# def root():
#     return {"test" : 1}

#a = {"test" : 1}