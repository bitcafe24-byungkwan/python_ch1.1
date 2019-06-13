"""
문제6
숨겨진 카드의 수를 맞추는 게임입니다. 1-100까지의 임의의 수를 가진 카드를 한 장 숨기고 이 카드의 수를 맞추는 게임입니다.
아래의 화면과 같이 카드 속의 수가 57인 경우를 보면 수를 맞추는 사람이 40이라고 입력하면 "더 높게", 다시 75이라고 입력하면
"더 낮게" 라는 식으로 범위를 좁혀가며 수를 맞추고 있습니다. 게임을 반복하기 위해 y/n이라고 묻고 n인 경우 종료됩니다.
"""
import random


def game_start():
    n = random.randrange(100) + 1
    print('수를 결정하였습니다. 맞추어 보세요')
    print('1-100')
    cnt = 1

    while 1:
        input_value = input("%d>>" % cnt)
        num = int(input_value)
        cnt += 1
        if num == n:
            print("맞았습니다.")
            break

        print("더 낮게 " if num > n else "더 높게")


game_flag = 'y'

while game_flag == 'y':
    game_start()
    game_flag = input("더하시겠습니까(y/n)>>")

