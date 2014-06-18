from urllib import request
from bs4 import BeautifulSoup
import os

choice = input("Enter '1' for tags '2' for popular images : (1 or 2) : ")
link = "http://weheartit.com/"
if choice == "1":
	tag = input("\nEnter tag : ")
	tag = tag.split(" ")
	tag = "%20".join(tag)
	link = link+"tag/"+tag
	popular = input("\nDo you want to download popular images only? y or n : ")
	if popular == 'y':
		year_check = input("\nDo you want a specific year? y or n : ")
		if year_check == 'y':
			year = input("\nEnter year : ")
			link = link+"/"+year
			month_choice = input("\nDo you want a specific month? : y or n : ")
			if month_choice == 'y':
				month = input("Enter month as corresponding number : ")
				if int(month) >= 1 and int(month) <=12:
					if len(month) == 1:
						month = "0"+month
					link = link+"/"+month
				else:
					print("You entered an invalid month. Try again. ")
					input()
					
elif choice == "2":
	year = input("Enter year : ")
	link = "http://weheartit.com/popular_images/"+year
	month_choice = input("Do you want a specific month? : y or n :")
	if month_choice == 'y':
		month = input("Enter month as corresponding number : ")
		if int(month) >= 1 and int(month) <=12:
			if len(month) == 1:
				month = "0"+month
			link = link+"/"+month
		else:
			print("You entered an invalid month. Try again. ")
			input()

else:
	print("Wrong choice try again.")
	input()

if link != "":
	print("\n"+link+"\n")
else:
	input()
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
	# print(x)
	n = x.get('href')
	# print(n)
	if n.find("entry") > -1:
		fi.write("http://weheartit.com"+str(n)+"\n")

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
	link = l
	#print(link)
	page = BeautifulSoup(request.urlopen(link),from_encoding="utf_8")
	n = page.find_all('img')
		
	for x in n:
		l = x.get("src")
		if l.find("large") > -1:
			s.add(l)

s = list(s)
for x in s:
	m.write(x+"\n")

print(len(s),"images to be downloaded...")
input("Press enter to continue...")

f.close()
m.close()

os.system("wget -P Images\ -i ilinks.txt")
os.system("del links.txt /q")
os.system("del ilinks.txt /q")
input()

path = str(os.getcwd())+'\\Images\\'

i=1
for file in os.listdir(path):
	current_file = os.path.join(path, file)
	if file.find("jpg") > -1 and not file.endswith("jpg"):
		os.rename(current_file, path+"{}.jpg".format(i))
	elif file.find("png") > -1 and not file.endswith("png"):
		os.rename(current_file, path+"{}.png".format(i))
	elif file.find("gif") > -1 and not file.endswith("gif"):
		os.rename(current_file, path+"{}.gif".format(i))
	i=i+1
