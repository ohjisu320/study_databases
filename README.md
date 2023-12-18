### mongodb functions

|명령어|설명|예시|pythons|
|--|--|--|--|
|insertOne()|row를 insert하는 명령어-넣는 값의 datatype이 dictionary|db.fruits.insertOne({...})|.insert_one()|
|insertMany()|list를 insert하는 명령어-넣는 값의 datatype이 list|db.fruits.insertMany([...])|.insert_many()|
|deleteOne()|key:value값과 동일한 row를 하나만 지우는 명령어|db.posts.deleteOne({ title: "Post Title 5" })|.delete.one()|
|deleteMany()|key:value값과 동일한 row를 여러개 지우는 명령어|db.posts.deleteMany({ category: "Technology" })|.delete.many()|
|deleteMany({})|해당하는 collection 안의 값 전체를 지우는 명령어|db.posts.deleteMany({})|.delete.many()|
|find()|해당하는 collection 안의 값 전체를 조회하는 명령어|db.fruits.find({})|.find()
|deleteMany({_id: ObjectId("")})|해당하는 collection 안의 행(들)을 objectid를 이용해서 삭제하는 명령어|db.fruits.deleteMany({_id: ObjectId("657a6e04d20aacdc51db7726")})|.delete.many({"_id": ObjectId("")})|
|find({},{_id : 1, title:1, category:1, likes:1, })|원하는 column head(머릿말)로 전체 행 조회하기|db.posts.find({},{_id : 1, title:1, category:1, likes:1, })|.find()
||다음 dict를 추출하는 명령어||documents.next()
|updateMany({:},{$set:{body:"update Post"}})|(조건에 맞는)여러 정보를 컬럼 단위로 변경하는 명령어|updateMany({category:{$eq:"Technology"}},{$set:{likes:1, body:"update Post", date:Date()}})|updateMany()
### MongoDB Query Operators

|명령어|설명|예시|pythons|
|--|--|--|--|
|$inc|value값을 증가시키는 key|db.posts.updateMany({}, { $inc : {likes : 10} }) ;|pythons|
|$eq|value값과 일치한다는 의미의 key|db.posts.find({category  :{ $eq : "Event"}},{title:1, category:1, likes:1});, db.fruits_colors.find({fruits_id:{$eq:ObjectId("657bf156f31b806c7897d9d3")}})|pythons|
|$gt|value값보다 큰 값들을 의미하는 key|db.posts.find({likes  :{ $gt : 4}},{title:1, category:1, likes:1});|pythons|
|$in|value값을 묶는 key|db.posts.find({category  :{ $in : ["Event", "Tech"]}},{title:1, category:1, likes:1});|pythons|
|$set|여러 value값을 조회할 때, 어떤 것들을 조회할 지 설정해주는 key|db.posts.
