# 5/23

# CRAPS游戏
# 玩家摇两颗骰子，如果第一次掷出了7点或11点，玩家胜；如果掷出了2点、3点或12点，庄家胜；
# 其他情况，游戏继续，玩家重新打骰子。如果玩家掷出了跟第一次相同的点数，玩家胜；如果玩家
# 掷出了7点，庄家胜；如果是其他点数，游戏继续，玩家重新打骰子，直到分出胜负。开始游戏时，玩家有1000元资产
# 每局游戏开始时，玩家下注，根据游戏的胜负赢得或输掉相应的注码，如果
# 玩家钱输光了，游戏结束。

import random
# random.randrange(1, 7) 生成[1,7)的随机数
frst_point = random.randrange(1, 7) + random.randrange(1, 7)
print(f'玩家掷出了{frst_point}点.')
if frst_point in (7, 11):
    print("玩家胜！")
elif frst_point in (2, 3, 12):
    print("庄家胜！")
else:
    while True:
        curr_point = random.randrange(1,7) +random.randrange(1,7)
        print(f'玩家掷出了{curr_point}点.')
        if curr_point == frst_point:
            print("玩家胜！")
            break
        elif curr_point == 7:
            print("庄家胜！")
            break

