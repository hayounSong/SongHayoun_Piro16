global num
num=0
global player1
player1="PlayerA"
global player2
player2="PlayerB"
global player
player=player2

class RangeError(Exception):
    def __init__(self):
        super().__init__('1,2,3 중 하나를 입력하세요')
def changeplayer():
    global player
    if player == player2:
        player = player1
    else:
        player = player2
def brGame():
    try:
        global player
        global num
        num_input = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
        if num_input > 3:
            raise RangeError
        changeplayer()
    except ValueError:
        print("정수를 입력해주세요")
    except RangeError:
        print('1,2,3 중 하나를 입력하세요')
    else:
        for i in range(0, num_input):
            num = num + 1
            print(player + ": " + str(num))
            if num == 31:
                break

while num<31:
    brGame()

changeplayer()

print(player,"win!")



