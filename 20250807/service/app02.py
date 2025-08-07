from typing import Annotated
from fastapi import Form

def get(txt : str):
    return {"test" : txt}

def post(txt : Annotated[str,Form(...)]):
    return {"test" : txt}

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
        }
    ]
}