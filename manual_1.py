n = map(int, input().split()) 

# これでnはスペース区切りで入力した整数のリストになります。 
# .split()は空白で分割された単語からなるリストを返します。 
# map(int,)は要素をint型にしたリストを返します。





class Test:
    def __init__(self, 引数1, 引数2, ….):
        #コンストラクタの定義
        





assert文とは
変数が期待する値ではない時に、例外を投げます。
デバッグやテストで使用します。
試行錯誤をしながらのアドホックなデータ分析の前処理等、「とにかく想定と違ったら止める」というだけで良いなら、unittest等のテストクラスを書かなくてよいassert文がお手軽です。

使い方
assert 条件式, 条件式がFalseの場合に出力するメッセージ
条件式が False の場合、AssertionError の例外が発生します。
条件式が True の場合は何も起こりません。

>>> kitai = 100
>>> input = 1
>>> assert kitai == input, '期待する値[{0}], 入力値[{1}]'.format(kitai, input)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: 期待する値[100], 入力値[1]







Pythonで小数点以下第３位まで表示して、それ以下は切り捨てて表示させたい

import decimal

v = 1.888888888
print('{:.3f}'.format(v))  # -> 1.889
print('{}'.format(round(v, 3)))  # -> 1.889

with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_FLOOR  # -∞方向に丸める ≒ 切り捨て
    v = round(decimal.Decimal(v), 3)    # 3桁, FLOORモードで丸め
print('{}'.format(v))  # -> 1.888

または

from decimal import (Decimal, ROUND_DOWN)

def round_down3(value):
    value = Decimal(value).quantize(Decimal('0.001'), rounding=ROUND_DOWN)
    return str(value)

print(round_down3(188888.8888888))
print(round_down3(1.8888899999))
print(round_down3(0.9999999999))
print(round_down3(-1.9999999999))

# 出力
# 188888.888
# 1.888
# 0.999
# -1.999






