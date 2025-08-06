from fastapi import FastAPI
from config import routers
app = FastAPI(**routers.config)

for ctr in routers.ctrs:
    app.include_router(**ctr)

# app = FastAPI(**routers.config)
# app.include_router(**routers.ctr1_config)
# app = FastAPI()
# @app.get("/")
# def root():
#     return a