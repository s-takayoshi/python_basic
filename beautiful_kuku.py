# きれいに整っているので見やすくなっています
# 式が表示されている
# 結果の桁数が違う場合は適切な量の半角スペースを挿入しているので、みやすい
# ※結果が3桁の場合は崩れてもOKです

line = int(input('行数を入力してください: '))
column = int(input('桁数を入力してください: '))

for x in range(1, line + 1):
    for y in range(1, column + 1):
        print(f'{x:2} ×{y:2} ={x * y:2} |',end=' ')
    print()
