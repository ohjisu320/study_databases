# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoClient=MongoClient("mongodb://localhost:27017/")
# collection 작업
local=mongoClient["local"]
# insert 작업 진행
collection=local["fruits"]

mix_fruit= {"name": "오렌지",
            "color": ["주황색", "갈색", "노란색"],
            "origin": "미국"}
result=collection.insert_one(mix_fruit)

pass