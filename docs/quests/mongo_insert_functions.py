from pymongo import MongoClient
mongoclient=MongoClient("mongodb://localhost:27017/")
local=mongoclient["local"]
fruits=local["fruits"]

local.fruits.insert_one(
    {"과일이름": "오렌지", "색상": "주황색", "원산지": "미국"}

)