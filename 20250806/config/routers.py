from controller import root

config = {
    "title" : "UV API",
    "version" : "0.0.1",
    "docs_url":"/api_docs",
    "redoc_ulr" : None
}

ctr1_config ={
    "router" : root.ctr1,
    "prefix" : "/ctr1",
    "tags" : ["기능1"]
}

ctr2_config ={
    "router" : root.ctr2,
    "prefix" : "/ctr2",
    "tags" : ["기능2"]
}

ctrs = [ctr1_config,ctr2_config]