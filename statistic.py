# スペース区切りで入力された整数群において、以下の4つの統計量を計算アプリを実装してください
# 合計値
# 最大値
# 最小値
# 平均値
# ただし、組み込み関数やライブラリは使わないこと(sum()やnp.mean()など)
# 1つの統計量につき、それ専用の関数を実装すること

def get_sum(numbers):
    sum_num = 0
    for num in numbers:
        sum_num += num
    return sum_num

def get_max(numbers):
    max_num = numbers[0]
    for i in range(1, len(numbers)):
        if max_num < numbers[i]:
            max_num = numbers[i]
    return max_num

def get_mini(numbers):
    mini_num = numbers[0]
    for i in range(1, len(numbers)):
        if mini_num > numbers[i]:
            mini_num = numbers[i]
    return mini_num

def get_ave(numbers):
    sum_num = get_sum(numbers)
    return sum_num / len(numbers)


input_str = input('データを入力してください(スペース区切り)＞')
number_list = []
for s in input_str.split(' '):
    number_list.append(int(s))

print(f'合計値: {get_sum(number_list)}')
print(f'最大値: {get_max(number_list)}')
print(f'最小値: {get_mini(number_list)}')
print(f'平均値: {get_ave(number_list)}')
