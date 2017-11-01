import urllib.request
from bs4 import BeautifulSoup
#req = urllib.request.urlopen("https://ja.wikipedia.org/wiki/%E3%83%A1%E3%82%A4%E3%83%B3%E3%83%9A%E3%83%BC%E3%82%B8")
req = urllib.request.urlopen("http://www.kintsuma2006.com/tokushima/web/schedule1.html")
soup = BeautifulSoup(req,"html.parser")
#contact = soup.find_all("p")
contact = soup.find_all("span")
for name in contact:
    print(name.get_text())
# print(isinstance(contact, list))
# for i in contact:
    # print(i)


#print(soup.find_all("span"))  #kt必要
# print(soup.find("a").text)
#print(soup.get('href')) 
#soup.select('<a href=')
# print(soup.find_all("apan", attrs={"class": "link", "href": "/link"})


# file型のオブジェクトを取得し、テキストファイルと接続する、モードは上書きモード。
# sample.txtが存在しない場合は、自動的に新規作成される。
f = open('sample.txt', 'w')
 
# テキストファイルに書き込む文字列
#sample_str = soup.find_all("span")
for name in contact:
    # print(name.get_text())
    f.write(name.get_text())
# テキストファイルへの書き込み
#f.write(str(sample_str))
 
# 移動中のデータをクリア
f.flush()
 
# テキストファイルとの接続を切る
f.close()