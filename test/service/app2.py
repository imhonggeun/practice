def get():
    return {"연습" : "get"}

practive = {
   "prefix":"/s2", 
   "tags":["기능2"],
   "urls" : [ 
    {
      "methods":["GET"], 
      "path":"/", 
      "endpoint": get,
    },
  ]
}
