
# def __init__() -> None:
    
def connectdb(colname):
    from pymongo import MongoClient    # mongodb에 접속 -> 자원에 대한 class
    mongoClient=MongoClient("mongodb://localhost:27017/")    # database 연결
    database=mongoClient["local"]    # collection 작업
    collection=database[colname]    # insert 작업 진행
    return collection

def insert_todo(todo_list_source): # 초기화 프로그램
    col_todos_list=connectdb("todos_list")
    col_todos_list.delete_many({})
    col_todos_list.insert_many(todo_list_source)
    return col_todos_list

todo_list_source = [
        {"title": "주간 보고서 작성", "description": "팀의 주간 성과와 진행 상황에 대한 보고서를 작성합니다."},
        {"title": "이메일 확인 및 응답", "description": "미처 확인하지 못한 이메일을 확인하고 필요한 이메일에 대해 응답합니다."},
        {"title": "회의 준비", "description": "다가오는 회의에 대해 준비합니다. 주제 연구, 발표 자료 준비 등이 포함될 수 있습니다."},
        {"title": "프로젝트 계획서 수정", "description": "현재 진행 중인 프로젝트의 계획서를 검토하고 필요한 부분을 수정합니다."},
        {"title": "팀 멤버와의 1:1 면담", "description": "팀 멤버와 개별적으로 만나서 그들의 업무 진행 상황, 이슈, 우려사항 등을 논의합니다."},]


class userint():
    def __init__(self) -> None:
        self.col_participants=connectdb("participants")
        pass
    def input_name(self) :
        self.col_todos_list=insert_todo(todo_list_source)
        self.username=input("Input Your Name:  ")
        self.inserted_username=self.col_participants.insert_one({"User":username})  # username에 User가 input한 값 넣기
    def userinterface(self):
        user_id=self.inserted_username.inserted_id # user_id는  User가 사용자가 입력한 username인 것의 id
        print("ToDo List 중 하나 선택 하세요 !")
        list_todos_list=list(self.col_todos_list.find({}))
        for count in range(len(list_todos_list)) :
            if count<4 :
                print("{}. {}".format(count+1, list_todos_list[count]["title"]),end=", ") 
            else :
                print("{}. {}".format(count+1, list_todos_list[count]["title"]))
        col_participants_todos=connectdb("participants_todos")
        title_input=int(input("Title 번호 : "))
        title_contents=list_todos_list[title_input-1]["title"]
        status=input("Status:  ")
        col_participants_todos.insert_one({"User_id":user_id, "User":self.username,"Title":title_contents, "Status":status})
        return self.end_sign()
    def end_sign(self):
        end_sign=input("종료 여부 : ")
        while True:
            if end_sign=="c" :
                self.userinterface()        
            elif end_sign=="q":
                self.input_name()
                self.userinterface()
            else :
                self.userinterface()   
        pass


# def repeater(end_sign):
#     userinterface()
#     while True :
#         if end_sign=="c" :
#             userinterface()
#         elif end_sign=="q" :
#             repeater()
#         elif end_sign=="x" :
#             print("프로그램이 종료되었습니다.")
#             break
#     return 
userint.input_name()    
userint.userinterface()




# user_id=connectdb("participants").find({"User":username},{"$set":{"_id":ObjectId()}})
# col_participants_todos.insert_one({"User_id":{"$eq":},"User":username,"Title" : title})

