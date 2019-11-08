# N面サイコロをM回振ったときの結果を表示してください
# N, M は正の整数とします
# N, M はユーザーからの入力を利用すること

import random

nuber_dice = int(input('サイコロの面の数は?:'))
shake_dice = int(input('何回振りますか?:'))

num_list = []
for i in range(shake_dice):
    num_list.append(random.randint(1, nuber_dice))
print(num_list)