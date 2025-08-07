from fastapi import FastAPI
from config import routers,info
app = FastAPI(**info.info_config)
for ctr in routers.ctrs:
  app.include_router(**ctr)
