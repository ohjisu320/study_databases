### mongodb functions

|명령어|설명|예시|pythons|
|--|--|--|--|
|insertOne()|row를 insert하는 명령어|db.fruits.insertOne({...})|.insert_one()|
|insertMany()|list를 insert하는 명령어|db.fruits.insertMany([...])|.insert_many()|
|deleteOne()|key:value값과 동일한 row를 하나만 지우는 명령어|db.posts.deleteOne({ title: "Post Title 5" })|.delete.one()|
|deleteMany()|key:value값과 동일한 row를 여러개 지우는 명령어|db.posts.deleteMany({ category: "Technology" })|.delete.many()|
|deleteMany()|해당하는 collection 안의 값 전체를 지우는 명령어|db.posts.deleteMany({})|.delete.many()|
|find()|해당하는 collection 안의 값 전체를 조회하는 명령어|db.fruits.find({})|
|db.fruits.deleteMany({_id: ObjectId("")})|해당하는 collection 안의 행(들)을 objectid를 이용해서 삭제하는 명령어|db.fruits.deleteMany({_id: ObjectId("657a6e04d20aacdc51db7726")})|.delete.many({"_id": ObjectId("")})|
