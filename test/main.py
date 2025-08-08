from fastapi import FastAPI
from config import routers,info
from fastapi.staticfiles import StaticFiles


app = FastAPI(**info.info_config)
for ctr in routers.ctrs:
  app.include_router(**ctr)

app.mount("/",StaticFiles(directory="static", html=True), name="static")