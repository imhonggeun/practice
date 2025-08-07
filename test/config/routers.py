from fastapi import APIRouter
from controller import root


ctrs = []
for link in root.urls:
  ctr = APIRouter()
  router = {
    "prefix": link["prefix"],
    "tags": link["tags"],
  }
  for item in link["urls"]:
    ctr.add_api_route(**item)
    
  router["router"] = ctr
  ctrs.append(router)
