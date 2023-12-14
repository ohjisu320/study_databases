
# mongodb에 접속 -> 접속 자원을 class로 지정(teacher : 자원에 대한 class)
def connect_mongo():
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    # database 연결
    database=mongoClient["local"]
    # collection에 작업
    dict_fruit_info=database['fruits_info']
    # insert 작업 진행
    return dict_fruit_info
# insert하는 function create
def insert_fruits(x) :
    fruits_info=connect_mongo()
    fruits_info.insert_many(x)
    return fruits_info

#insert할 변수 설정
fruits_add =fruit_info = [
    {"name": "사과", "color": "빨간색", "origin": "한국"},
    {"name": "바나나", "color": "노란색", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황색", "origin": "미국"}
]
# connect_mongo() function 실행
connect_mongo()
# insert_fruits에 insert할 변수 넣어서 실행
insert_fruits(fruits_add)
pass