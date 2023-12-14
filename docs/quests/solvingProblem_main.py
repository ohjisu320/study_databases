# db와 연결함
def connect_mongo(collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient["local"]
    dict_fruit_info=database[collection_name]
    dict_fruit_info.delete_many({})
    return dict_fruit_info
solvingProblem=connect_mongo("solvingProblem")
# 문제와 답안을 DB에 넣어줌
quiz_list = [
        {
            "question": "Python의 생성자 함수 이름은 무엇인가요?",
            "choices": ["__init__", "__main__", "__str__", "__del__"],
            "answer": "__init__",
            "score": 20
        },
        {
            "question": "Python에서 'Hello, World!'를 출력하는 코드는 무엇인가요?",
            "choices": ["print('Hello, World!')", "console.log('Hello, World!')", "printf('Hello, World!')", "echo 'Hello, World!'"],
            "answer": "print('Hello, World!')",
            "score": 20
        },
        {
            "question": "Python의 주석을 나타내는 기호는 무엇인가요?",
            "choices": ["//", "/* */", "#", "--"],
            "answer": "#",
            "score": 20
        },
        {
            "question": "Python에서 리스트의 길이를 반환하는 함수는 무엇인가요?",
            "choices": ["size()", "length()", "len()", "sizeof()"],
            "answer": "len()",
            "score": 20
        },
        {
            "question": "Python에서 문자열을 숫자로 변환하는 함수는 무엇인가요?",
            "choices": ["str()", "int()", "char()", "float()"],
            "answer": "int()",
            "score": 20
        }
    ]
def quiz_connect() :
    solvingProblem.insert_many(quiz_list)

# 사용자 답변을 DB에 넣어줌
# 사용자 답변 자리 생성
solvingProblem.update_one({},{"$set":{"user_answer":0}})
solvingProblem.update_one({},{"$set":{"number":0}})
def useranswer_connect():
    list_quiz_useranswer=[]
    dict_quiz_useranswer={}
    for count in range(len(quiz_list)) :
        dict_quiz_useranswer={"user_answer" : input("answer : ")}
    return dict_quiz_useranswer
quiz_connect()

dict_useranswer=useranswer_connect()
for count in range(len(quiz_list)) :
    solvingProblem.insert_one({solvingProblem[count-1]},{"$set":{"user_answer":dict_useranswer}})


# 문제 > 답안 > 사용자답변 순으로 function 작동하도록 함. 
