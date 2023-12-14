
# collection_name에 생성할 collection의 이름을 넣을 것임
def connect_mongo(collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient["local"]
    dict_fruit_info=database[collection_name]
    return dict_fruit_info
# insert하는 function create
def insert_fruits(x) :
    fruits_info.insert_many(x)
    return fruits_info

#insert할 변수 설정
fruits_add = [
    {"name": "사과", "color": "빨간색", "origin": "한국"},
    {"name": "바나나", "color": "노란색", "origin": "필리핀"},
    {"name": "키위", "color": "갈색", "origin": "뉴질랜드"},
    {"name": "오렌지", "color": "주황색", "origin": "미국"}
]
fruits_info=connect_mongo( "fruits_info") # 내가 생성할(사용할) collection 이름=fruits_info
# insert_fruits에 insert할 변수 넣어서 실행
insert_fruits(fruits_add) 
pass