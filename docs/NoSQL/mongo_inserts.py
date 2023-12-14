# mongodb에 접속 -> 자원에 대한
from pymongo import MongoClient
# 
mongoclient=MongoClient("mongodb://localhost:27017/")
# collection 작업
collection=mongoclient["local"]
# insert 작업 진행
fruits=collection["fruits"]

local.fruits.insert_one(
    {"과일이름": "오렌지", "색상": "주황색", "원산지": "미국"})

result = collection.insert_one(dic_fruit)