파일생성
# uv init 
폴더 이동
# cd 폴더명


설치
# uv add streamlit

실행
# uv run streamlit hello

uv로 파일 실행 
# uv run streamlit run main.py 

패키지 설치(의존성 추가)
# uv add pandas matplotlib streamlit lxml 이렇게도 추가 가능
# uv add lxml
# uv add matplotlib
# uv add pandas
# uv add streamlit

fastapi 실행
# uv run fastapi dev

fastapi 실행
# uv add fastapi --extra standard
main.py
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root():
    return {"test" : 1}


정적파일 설정 main.py
# 아래 내용 fastapi 
# from fastapi.staticfiles import StaticFiles
# app.mount("/",StaticFiles(directory="static", html=True), name="static")

파일 업로드
# uv add python-multipart
from typing import Annotated
from fastapi import Form
# 추가
from fastapi import File, UploadFile
import os,shutil
from fastapi.responses import FileResponse
import mimetypes
from uuid import uuid4