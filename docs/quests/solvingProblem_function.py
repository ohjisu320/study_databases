# db와 연결함
def connect_mongo(collection_name):
    from pymongo import MongoClient
    mongoClient=MongoClient("mongodb://localhost:27017")
    database=mongoClient["local"]
    dict_fruit_info=database[collection_name]
    dict_fruit_info.delete_many({})
    return dict_fruit_info
# solvingProblem=connect_mongo("solvingProblem")

def quiz_connect(quiz_list) :
    solvingProblem=connect_mongo("solvingProblem")
    solvingProblem.insert_many(quiz_list)

def quiz_print(collection) :
    solvingproblem = collection.find({})
    print("아래는 5개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화")
    for i in range(5) :
        print("문제{}.{}".format(i+1, solvingproblem[i]["question"]))
        for j in range(4) :
            print("{}.{}".format(j+1, solvingproblem[i]["choices"][j]))
        useranswer = int(input("답을 입력하세요: "))
        collection.update_one({"_id":solvingproblem[i]["_id"]},{"$set":{"user_answer":useranswer}})
        if useranswer == solvingproblem[i]["answer_number"]:
            print("정답입니다!")
        else :
            print("틀렸습니다.")
        print("")
    