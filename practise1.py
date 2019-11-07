# A-1:"Bob", "Tom", "Ken" という3つの文字列要素を持つusersというリストを定義
user = ["Bob", "Tom", "Ken"]

# A-2:1から5までの整数を要素として持つint_numbersリストを定義
int_number = [1, 2, 3, 4, 5]

# A-3:"Kazuma", "Takahashi", 35 という 3つの要素をもつkazuma_infoというリストを定義
kazuma_info = ["Kazuma", "Takahashi", 35]

# A-4:リストから "Makoto" と "Kazuma" を取得して出力
members = ["Kazuma", "Makoto", "Ohira"]
print(members[1])
print(members[0])

# A-5:次のリストを利用して、"Name: Takahashi Kazuma, Age: 35"と出力
kazuma_info = ["Kazuma", "Takahashi", 35]
print(f'Name:{kazuma_info[1]} {kazuma_info[0]},Age:{kazuma_info[2]}')

# A-6:for を使って odd_numbers の各要素を出力
odd_numbers = [1, 3, 5, 7, 9]

for number in(odd_numbers):
    print(number)

# A-7:for を使って even_numbers のそれぞれの値を2倍した値を出力

even_numbers = [2, 4, 6, 8]

for multiple in(even_numbers):
    print(multiple * 2)

# A-8:users_info を使って次のような出力をしてください
# Name: Kazuma, Age: 35
# Name: Tom, Age: 57
# Name: Bob, Age: 77
users_info = [["Kazuma", 35],
              ["Tom", 57],
              ["Bob", 77]]

for name in(users_info):
    print(f'Name: {name[0]}, Age: {name[1]}')


# A-9:下記のコードが期待通り動作するような辞書を定義してください
# print(kazuma_info["first_name"]) # "Kazuma"
# print(kazuma_info["family_name"]) # "Takahashi"
# print(kazuma_info["age"]) # 35
kazuma_info = {"first_name": "Kazuma", "family_name": "Takahashi", "age": 35}
print(kazuma_info["first_name"]) # "Kazuma"
print(kazuma_info["family_name"]) # "Takahashi"
print(kazuma_info["age"]) # 35

# A-10:1から6の整数をランダムに出力する dice() 関数を実装してください
import random
def dice():
    print(random.randint(1,6))

# A-11:身長(m)と体重(kg)を入力として受け取りBMIを計算するアプリを実装してください
# 参考となるWebアプリ https://keisan.casio.jp/exec/system/1161228732
# 小数点第2位まで表示すること

height = int(input('身長は(m)？＞')) / 100
weight = int(input('体重は(kg)？＞'))

bmi = weight / height ** 2
print(f'{bmi:.2f}')