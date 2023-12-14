### mongodb functions

|명령어|설명|예시|
|--|--|--|
|insertOne()|row를 insert하는 명령어|db.fruits.insertOne({...})|
|insertMany()|list를 insert하는 명령어|db.fruits.insertMany([...])|
|deleteOne()|key:value값과 동일한 row를 하나만 지우는 명령어|db.posts.deleteOne({ title: "Post Title 5" })|
|deleteMany()|key:value값과 동일한 row를 여러개 지우는 명령어|db.posts.deleteMany({ category: "Technology" })|
|deleteMany()|해당하는 collection 안의 값 전체를 지우는 명령어|db.posts.deleteMany({})|