
#예외처리 클래스들
class RangeError(Exception):
    def __init__(self):
        super().__init__("Score is not positive Integer")


class SamenameError(Exception):
    def __init__(self):
        super().__init__("Already exist Name!")


class Notmatch(Exception):
    def __init__(self):
        super().__init__("Num of Data is not 3!!")
class Nostudent(Exception):
    def __init__(self):
        super().__init__("No student Data!")
class GradeError(Exception):
    def __init__(self):
        super().__init__("There is a student who didn't get grade")
##############  menu 1
def Menu1(name,middle,final):
    S = student(name,middle,final)
    DBstudent.append(S)
##############  menu 2

def Menu2():
    for i in DBstudent:
        rate = (int(i.mid) + int(i.final)) / 2
        if rate >= 90:
            i.grade = 'A'
        elif rate >= 80:
            i.grade = 'B'
        elif rate >= 70:
            i.grade = 'C'
        else:
            i.grade = 'D'
    print("Grading to all student")
    #매개변수가 필요한지 판단 후 코딩할 것 :
    #학점 부여 하는 코딩

##############  menu 3
def Menu3():
    print("----------------------")
    print("name mid final grade")
    print("----------------------")
    for i in DBstudent:
        print(i.name + "  " + i.mid + "  " + i.final + "  " + i.grade)

    #매개변수가 필요한지 판단 후 코딩할 것) :
    #출력 코딩

##############  menu 4
def Menu4(inputname):

    for i in range(0, len(DBstudent)):
        if DBstudent[i].name == inputname:
            del DBstudent[i]
            print(inputname + " student information is deleted.")
            break
    #매개변수가 필요한지 판단 후 코딩할 것):
    #학생 정보 삭제하는 코딩


#학생 정보를 저장할 변수 초기화
class student:
    grade=""
    def __init__(self,name,mid,final):
        self.name=name
        self.mid=mid
        self.final=final


DBstudent = []


print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")

    if choice == "1":


       while True:
            try:
                Inputs=input('Enter name mid-score final-score : ').split()
                if len(Inputs)!=3:
                    raise Notmatch
                for i in DBstudent:
                    if Inputs[0] == i.name:
                        raise SamenameError
                if int(Inputs[1])<=0 or int(Inputs[2])<=0:
                    raise RangeError


            except RangeError:
                print("Score is not positive Integer")
            except ValueError:
                print("이름,성적,성적 순으로 입력해주세요 순서가 잘못되엇습니다.")
            except SamenameError:
                print("Already exist Name!")
            except Notmatch:
                print("Num of Data is not 3!!")
            else:
                break

       Menu1(Inputs[0],Inputs[1],Inputs[2])


        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출

    elif choice == "2" :
        try:
            if len(DBstudent)==0:
                raise Nostudent

        except Nostudent:
            print("No student Data!")
        else:
            Menu2()

    # 예외사항 처리(저장된 학생 정보의 유무)
    # 예외사항이 아닌 경우 2번 함수 호출
    # "Grading to all students." 출력

    elif choice == "3" :

        try:
            if len(DBstudent)==0:
                raise Nostudent
            for a in DBstudent:
                if a.grade=="":
                    raise GradeError
        except Nostudent:
            print("No student Data!")
        except GradeError:
            print("There is a student who didn't get grade")
        else:
            Menu3()

        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :

        try:
            if len(DBstudent)==0:
                raise Nostudent

        except Nostudent:
            print("No student Data!")
        else:
            inputname=input("Enter the name to delete : ")
            count=0
            for A in DBstudent:
                if A.name==inputname:
                    count=count+1
            if count==0:
                print("Not exist name!")
            else:
                Menu4(inputname)



        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!")
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number,Choose again")
        #"Wrong number. Choose again." 출력
