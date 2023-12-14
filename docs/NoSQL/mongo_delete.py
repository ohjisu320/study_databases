# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoClient=MongoClient("mongodb://localhost:27017/")
# collection 작업
local=mongoClient["local"]
# insert 작업 진행
collection=local["fruits"]

list_fruit= [
    {"name": "사과", "color": "빨간색", "origin": "한국"},
    {"name": "바나나", "color": "노란색", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황색", "origin": "미국"}
]
insert_result = collection.insert_many(list_fruit)
# fruits 안의 값 전체삭제
## fruits.delete_many({})

# object id로 삭제 = delete inserted records by _ids
## .inserted_ids = insert_result 안에 들어간 값들의 id를 받아내는 function
list_inserted_ids=insert_result.inserted_ids
collection.delete_many({"_id":list_inserted_ids[0]})

pass
