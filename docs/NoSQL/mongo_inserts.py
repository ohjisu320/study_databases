# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoClient=MongoClient("mongodb://localhost:27017/")
# collection 작업
database=mongoClient["local"]
# insert 작업 진행
collection=database["fruits"]

dict_fruits = {"과일이름": "오렌지", "색상": "주황색", "원산지": "미국"}

result = collection.insert_one(dict_fruits)

local.fruits.insert_one(
    {"과일이름": "오렌지", "색상": "주황색", "원산지": "미국"})