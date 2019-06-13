"""
문제4
반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
출력해보세요. 1부터 99까지만 실행하세요

"""
for game_num in range(1, 100):
    cnt = str(game_num).count('3') + str(game_num).count('6') + str(game_num).count('9')
    if cnt:
        print("%d %s" % (game_num, '짝' * cnt))
