# mongodb에 접속 -> 자원에 대한 class
from pymongo import MongoClient
# database 연결
mongoClient=MongoClient("mongodb://localhost:27017/")
# collection 작업
local=mongoClient["local"]
# insert 작업 진행
collection=local["posts"]

# documents - collection 안의 값
# cursor? - 단계별로 된다? --> 전체 사이즈를 모르기에 length를 사용할 수 없다.
# cast cursor to list
documents = collection.find({}, {"_id  ":1, "title":1, "likes":1})
list_documents = list(documents)
print("list_documents_length : {}".format(len(list_documents)))
# [{'_id': ObjectId('657a8e08aa...0aeb1f78'), 'title': 'Post Title 3', 'likes': 1}, {'_id': ObjectId('657a8e08aa...0aeb1f79'), 'title': 'Post Title 4', 'likes': 115}, {'_id': ObjectId('657a9cecaa...0aeb1f7a'), 'title': 'Post Title 2', 'likes': 2}, {'_id': ObjectId('657a9cecaa...0aeb1f7b'), 'title': 'Post Title 3', 'likes': 1}, {'_id': ObjectId('657a9cecaa...0aeb1f7c'), 'title': 'Post Title 4', 'likes': 4}]
for document in list_documents :
    print("document : {}".format(document))
    print("list_documents_length : {}".format(len(list_documents)))
pass
