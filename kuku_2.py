# 下記のような出力が得られる kuku_2.py を実装してください
# 任意の行数および任意の列数での掛け算の結果が得られます

line = int(input('行数を入力してください: '))
column = int(input('桁数を入力してください: '))

for x in range(1, line + 1):
    for y in range(1, column + 1):
        print(x * y, end=' ')
    print()
