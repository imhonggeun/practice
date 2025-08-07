from fastapi import FastAPI
from config import info, routes
from fastapi.staticfiles import StaticFiles


app = FastAPI(**info.api_config)
for route in routes.ctrs:
  app.include_router(**route)

app.mount("/",StaticFiles(directory="static", html=True), name="static")