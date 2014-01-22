from urllib import request
from bs4 import BeautifulSoup
import os

choice = input("Enter 1 for tag 2 for popular images' year : ")
link = ""
if choice == "1":
	tag = input("Enter tag : ")
	tag = tag.split(" ")
	tag = "%20".join(tag)
	link = "http://weheartit.com/tag/"+tag
elif choice == "2":
	year = input("Enter year : ")
	link = "http://weheartit.com/popular_images/"+year
	month_choice = input("Do you want a specific month? : y or n ")
	if month_choice == 'y':
		month = input("Enter month as corresponding number : ")
		if int(month) >= 1 and int(month) <=12:
			if len(month) == 1:
				month = "0"+month
			link = link+"/"+month
		else:
			print("You entered an invalid month. Try again. ")

if link != "":
	print("\n"+link+"\n")
else:
	os.sys.exit()
# Get links of entries

print("Getting list of entries in the page...\n")

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

print("Getting list of images for each entry...")

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
			if l.endswith("large.jpg") or l.endswith("large.png"):
				s.add(l)

s = list(s)
for x in s:
	m.write(x+"\n")

print(len(s),"images to be downloaded...")
input("Press enter to continue...")
f.close()
m.close()

os.system("wget -P Images/ -i ilinks.txt")
