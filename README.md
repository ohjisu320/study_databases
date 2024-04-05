### MongoDB functions

<details>
<summary>접기/펼치기</summary>

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

 </details> 


### MongoDB Query Operators

<details>
<summary>접기/펼치기</summary>

|명령어|설명|예시|pythons|
|--|--|--|--|
|$inc|value값을 증가시키는 key|db.posts.updateMany({}, { $inc : {likes : 10} }) ;|pythons|
|$eq|value값과 일치한다는 의미의 key|db.posts.find({category  :{ $eq : "Event"}},{title:1, category:1, likes:1});, db.fruits_colors.find({fruits_id:{$eq:ObjectId("657bf156f31b806c7897d9d3")}})|pythons|
|$gt|value값보다 큰 값들을 의미하는 key|db.posts.find({likes  :{ $gt : 4}},{title:1, category:1, likes:1});|pythons|
|$in|value값을 묶는 key|db.posts.find({category  :{ $in : ["Event", "Tech"]}},{title:1, category:1, likes:1});|pythons|
|$set|여러 value값을 조회할 때, 어떤 것들을 조회할 지 설정해주는 key|db.posts.

 </details> 

### NoSQL with pythons

<details>
<summary>접기/펼치기</summary>

|구분|설명|링크|
|--|--|--|
|Inserts|DB에 Dictionary 형태로 data 넣기|[mongo_inserts.py](./docs/NoSQL/mongo_inserts.py)[mongo_inserts_doubleCollection.py](./docs/NoSQL/mongo_inserts_doubleCollection.py)|
|Finds|DB에서 원하는 key:value 찾기|[mongo_inserts.py](./docs/NoSQL/mongo_finds.py)|
|Deletes|DB에서 전체 or 특정 record 삭제|[mongo_delete.py](./docs/NoSQL/mongo_delete.py)|


 </details> 

### Quests

<details>
<summary>MongoDB</summary>

|구분|설명|링크|
|--|--|--|
|Inserts|function으로 data 넣기|[mongo_inserts.py](./docs/quests/mongo_insert_functions.py)|
|CRU|DB에 data 넣고 사용자 입력 값과 비교해 채점(정답 판별)|[solvingProblem_main.py](./docs/quests/solvingProblem_main.py)[solvingProblem_function.py](./docs/quests/solvingProblem_function.py)|
|CRU|DB에 data 넣고 사용자에게 보여준 후, 사용자 입력 값을 다른 DB에 insert|[todolist_main.py](./docs/quests/todolist_main.py)[todolist_function.py](./docs/quests/todolist_function.py)[display](./docs/img/todolist_main.png)|

 </details> 

<details>
<summary>MYSQL</summary>

|구분|설명|링크|
|--|--|--|
|SELECT|SELECT, GROUP BY, WHERE-IN, ORDER BY, HAVING을 이용한 예제풀이 퀘스트|[select_group_havings_orderby.sql](docs\SQLs\quests\select_group_havings_orderby.sql)|
|SELECT|INNER JOIN 활용한 예제풀이|[select_joins.sql](docs\SQLs\quests\select_joins.sql)
|SELECT|SUBQUERY와 이전 학습내용을 활용한 예제 풀이|[select_subquerys.sql](docs\SQLs\quests\select_subquerys.sql)|
|SELECT|이전 학습 내용 전부를 활용한 예제 풀이|[select_alls.sql](docs\SQLs\quests\select_alls.sql)|
|COMMON CODE|COMMON CODE TABLE을 활용한 JOIN|[common_codes.sql](docs\SQLs\quests\common_codes.sql)|

 </details> 