from urllib import request
from bs4 import BeautifulSoup
import os


tag = input("Enter tag : ")
tag = tag.split(" ")
tag = "%20".join(tag)
link = "http://weheartit.com/tag/"+tag
print(link+"\n")
# Get links of entries

page = request.urlopen(link)
content = page.read()
soup = BeautifulSoup(content,from_encoding="utf_8")
links = soup.find_all('a')
#print(p)

rs = set()

fi = open("links.txt","w+",encoding="utf_8")

for x in links:
	n = x.get('href')
	if n.startswith("http") and n.find("entry") > -1:
	 	fi.write(str(n)+"\n")

fi.close()

# Get the list of image links

f = open("links.txt","r",encoding="utf_8")
m = open("ilinks.txt","w+",encoding="utf_8")

k = f.read()
c = k.count("\n")
f.seek(0)
s = set()

for x in range(c):
	l = f.readline()
	if l.find("page") == -1:
		link = l
		#print(link)
		page = BeautifulSoup(request.urlopen(link),from_encoding="utf_8")
		n = page.find_all('img')
		
		for x in n:
			l = x.get("src")
			if l.endswith("large.jpg"):
				s.add(l)

s = list(s)
for x in s:
	m.write(x+"\n")

f.close()
m.close()

os.system("wget -i ilinks.txt")