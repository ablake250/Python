import requests
from bs4 import BeautifulSoup

URL = "https://na.op.gg/champion/statistics"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')

body = soup.findAll("div", {"class":"champion-index__champion-item"})

suppCounter = 0
topCounter = 0
midCounter = 0
botCounter = 0
jungCounter = 0

for i in body:
    if 'Support' in i.text:
        suppCounter += 1
    if "Top" in i.text:
        topCounter += 1
    if "Middle" in i.text:
        midCounter += 1
    if "Bottom" in i.text:
        botCounter += 1
    if "Jungle" in i.text:
        jungCounter += 1


print("\n\nUsing na.op.gg stats, this program will find all champions given a role.")
print("\nBelow shows the number of champions per role")
print ("\nTop:    \t", suppCounter)
print ("Jungle: \t", jungCounter)
print ("Middle: \t", midCounter)
print ("Bottom: \t", botCounter)
print ("Support: \t", suppCounter, "\n\n\n")

choice = input('Select a role: ')


if choice in ["Top", "Jungle", "Middle", "Bottom", "Support", "Bot", "Supp","Mid"]:
    print("\nThe champions below are all considered", choice, "laners:\n")
    for i in body:
        if str(choice) in i.text:
            champs += i.find('div',{"class":"champion-index__champion-item__name"}).text
            print (i.find('div',{"class":"champion-index__champion-item__name"}).text)
    print("\n\nGood luck!\n\n")
else:
    print("\nError: Choice Invalid\n\n")

print(champs)