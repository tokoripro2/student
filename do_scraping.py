import urllib.request
from bs4 import BeautifulSoup
req = urllib.request.urlopen("http://www.bookoffonline.co.jp/otona/CSfTop.jsp?bg=set")
#req = urllib.request.urlopen("http://www.kintsuma2006.com/tokushima/web/schedule1.html")
soup = BeautifulSoup(req,"html.parser")
#print(soup.find_all("a"))

#print(soup.find_all("span"))  #kt必要
# print(soup.find("a").text)
#print(soup.get('href')) 
#soup.select('<a href=')
# print(soup.find_all("apan", attrs={"class": "link", "href": "/link"})


# file型のオブジェクトを取得し、テキストファイルと接続する、モードは上書きモード。
# sample.txtが存在しない場合は、自動的に新規作成される。
f = open('sample.txt', 'w')
 
# テキストファイルに書き込む文字列
sample_str = soup.find_all("strong")
 
# テキストファイルへの書き込み
f.write(str(sample_str))
 
# 移動中のデータをクリア
f.flush()
 
# テキストファイルとの接続を切る
f.close()