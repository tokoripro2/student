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



文字列を逆にする

>>> s = 'abc-xyz'
>>> s[::-1]
'zyx-cba'

スライス

[::-1]とは
[0:-1:-1]のこと
1番目は文字列の最初からという意味
2番目は文字列の指定した番号までという意味マイナス(-)がつくと
    0より前なので全てということ
3番目は1番目に何個足してチェックするかという意味
    マイナス(-)がつくと後ろからという意味
    数字が増えると足して後ろからという意味
    
    
    

文字列の長さを計算する

s = 'abcdef'
print len(s)
u = u"ほげ"
print len(u)



文字列を2文字ずつ分割する

import re
buf='abcdef'
list = re.split('(..)',buf)[1::2]
print list

    


一部の文字を省く
変数.replace('省きたい文字', '')
省きたい文字はドット.で続けて入力することができる




引数で指定したオブジェクトが持つ値が要素の中に含まれている場合は、
最初の要素のインデックスを返します。

list = ["A", "B", "C"]
print list.index("B")     # 1

指定した値が存在しない場合には「ValueError」が発生します。
インデックスは"0"から始まる為何個目の場合は＋１が必要