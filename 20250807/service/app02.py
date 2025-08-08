from typing import Annotated
from fastapi import Form, File, UploadFile
import os,shutil
from fastapi.responses import FileResponse
import mimetypes
from uuid import uuid4

#저장 위치 설정 및 생성
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)


def post(txt : Annotated[str,Form(...)],file : UploadFile = File(...)):
    
    #fileName = file.filename
    ext = file.filename.split(".")[-1]
    fileName = f"{uuid4().hex}.{ext}" 
    filePath = os.path.join(UPLOAD_DIR, fileName)
    
    #파일 저장 부분
    with open(filePath, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
        
    return {"test" : txt, "name" : file.filename, "fileName" : fileName}

def read(fileName : str):
    filePath = os.path.join(UPLOAD_DIR, fileName)
    mediaType, _ = mimetypes.guess_type(filePath)
    headers ={
        "Content-Disposition" : f"inline; filename='{fileName}'"
    }
    return FileResponse(path=filePath, media_type=mediaType, filename=fileName, headers=headers)
    #return {"result" : "read()" }
    
def get(txt : str):
    return {"test" : txt }

study02 = {
    "prefix":"/s2",
    "tags":["연습2"],
    "urls" : [
        {
            "methods" : ["GET"],
            "path" : "/",
            "endpoint" : get
        },
        {
            "methods" : ["POST"],
            "path" : "/",
            "endpoint" : post
        },
        {
            "methods" : ["GET"],
            "path" : "/read",
            "endpoint" : read
        }
    ]
}