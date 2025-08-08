def get(txt):
    return {"연습" : txt}

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
