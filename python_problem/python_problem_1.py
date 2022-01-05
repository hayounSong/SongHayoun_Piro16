num=0

class RangeError(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')

while True:
    try:
        num_input=int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if num_input>3:
            raise RangeError
    except ValueError:
        print("정수를 입력해주세요")
    except RangeError:
        print('1,2,3 중 하나를 입력하세요')
    else:
        for i in range(0,num_input):
            num=num+1
            print("PlayerA: "+str(num))

        break