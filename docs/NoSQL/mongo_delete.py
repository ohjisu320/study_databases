# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoclient=MongoClient("mongodb://localhost:27017/")
# collection 작업
collection=mongoclient["local"]
# insert 작업 진행
fruits=collection["fruits"]

list_fruit= [
    {"name": "사과", "color": "빨간색", "origin": "한국"},
    {"name": "바나나", "color": "노란색", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황색", "origin": "미국"}
]
result = fruits.insert_many(list_fruit)
