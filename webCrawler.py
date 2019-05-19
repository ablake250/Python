import requests
from bs4 import BeautifulSoup
import csv

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
        suppCounter = suppCounter + 1
    if "Top" in i.text:
        topCounter = topCounter + 1
    if "Middle" in i.text:
        midCounter = midCounter + 1
    if "Bottom" in i.text:
        botCounter = botCounter + 1
    if "Jungle" in i.text:
        jungCounter = jungCounter + 1

print '\n\n\n',"Top:    \t", suppCounter
print "Jungle: \t", jungCounter
print "Middle: \t", midCounter
print "Bottom: \t", botCounter
print "Support: \t", suppCounter, "\n\n\n"

choice = raw_input('Choose list of Champtions by Role: ')


print(choice)

for i in body:
    if str(choice) in i.text:
        print i.content
