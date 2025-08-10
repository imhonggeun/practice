from typing import Annotated
from fastapi import Form, File, UploadFile
from fastapi.responses import FileResponse
import os, shutil
import mimetypes
from uuid import uuid4
import pymysql
from config.info import DB_CONFIG

# ===== 📁 업로드 디렉토리 설정 =====
UPLOAD_DIR = "uploaded_images"
os.makedirs(UPLOAD_DIR, exist_ok=True)



# ===== 💾 이미지 저장 (MariaDB) =====
def save_image_to_db(file_name: str, image_bytes: bytes):
    try:
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = "INSERT INTO image (file_name, image_data) VALUES (%s, %s)"
        cursor.execute(sql, (file_name, image_bytes))
        conn.commit()
    finally:
        conn.close()

# ===== 📥 POST - 파일 업로드 처리 =====
def post(txt: Annotated[str, Form(...)], file: UploadFile = File(...)):
    ext = file.filename.split(".")[-1]
    fileName = f"{uuid4().hex}.{ext}"
    filePath = os.path.join(UPLOAD_DIR, fileName)

    # 업로드 파일의 바이너리 데이터를 읽기
    image_bytes = file.file.read()

    # 로컬 저장
    with open(filePath, "wb") as f:
        f.write(image_bytes)

    # DB 저장
    save_image_to_db(fileName, image_bytes)

    return {"test": txt, "originalName": file.filename, "savedFile": fileName}


# ===== 📤 파일 읽기 API =====
def read(fileName: str):
    filePath = os.path.join(UPLOAD_DIR, fileName)
    mediaType, _ = mimetypes.guess_type(filePath)
    headers = {
        "Content-Disposition": f"inline; filename='{fileName}'"
    }
    return FileResponse(path=filePath, media_type=mediaType, filename=fileName, headers=headers)

# ===== 🧪 테스트 GET =====
def get(txt: str):
    return {"test": txt}

# ===== 🔗 FastAPI 라우터 정보 =====
study02 = {
    "prefix": "/s2",
    "tags": ["연습2"],
    "urls": [
        {"methods": ["GET"], "path": "/", "endpoint": get},
        {"methods": ["POST"], "path": "/", "endpoint": post},
        {"methods": ["GET"], "path": "/read", "endpoint": read}
    ]
}
