# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoClient=MongoClient("mongodb://localhost:27017/")
# collection 작업
database=mongoClient["local"]
# insert 작업 진행
collection=database["fruits"]

# 분리 입력 (fruits, fruits_colors)
# insert fruits 작업 진행
dict_fruit= {"name": "오렌지",
            "origin": "미국"}
result=collection.insert_one(dict_fruit)
# insertedId: ObjectId("657bf156f31b806c7897d9d3")
# 이 아래부분 이해 안감
print("result.inserted_id : {}".format(result.inserted_id))
inserted_id=result.inserted_id

# insert fruits_colors 작업 진행
# [{"fruits_id" :ObjectId("657bf156f31b806c7897d9d3"), "color":"주황색"},
# {"fruits_id" :ObjectId("657bf156f31b806c7897d9d3"),"color":"갈색"},
# {"fruits_id" :ObjectId("657bf156f31b806c7897d9d3"),"color":"노란색"}]
fruits_colors=[{"color":"주황색"},
                {"color":"갈색"},
                {"color":"노란색"}]

list_fruits_colors = list()
for dict_color in fruits_colors :
    dict_color["fruits_id"]=inserted_id
    list_fruits_colors.append(dict_color)
pass 

# collection fruits_colors 
collection_fruits_colors = database["fruits_colors"]
collection_fruits_colors.insert_many(list_fruits_colors)
# find from fruits_colors
documents=collection_fruits_colors.find({"fruits_id":{"$eq":inserted_id}})
pass
# db.fruits_colors.find({fruits_id:{$eq:ObjectId("657bf156f31b806c7897d9d3")}});