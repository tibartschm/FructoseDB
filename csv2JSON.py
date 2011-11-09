#! /usr/bin/python

import json

nutComps = []
dkTab2 = open("DK-TAB2.csv")
dkTab2.next()
for line in dkTab2:
	line = unicode(line, encoding="iso_8859_1")
	line = line.strip()
	cells = line.split(";")
	for i in range(5):
		cells[i] = cells[i].strip()
	nutComp = {"compId": cells[0], "SrtOrd": cells[1], "Unit": cells[2], "CmpNameDK": cells[3], "CmpNameEN": cells[4]}
	nutComps.append(nutComp)
dkTab2.close()


foods = []
dkTab1 = open("DK-TAB1.csv")
dkTab1.next()
dkTab1.next()
for line in dkTab1:
	line = unicode(line, encoding="iso_8859_1")
	line = line.strip();
	nutritions = line.split(";")
	food = {"Name-EN": nutritions[2], "Name-DK": nutritions[1]}
	i = 0
	for i in range(1, len(nutComps) -1):
		if nutritions[i]:
			food[nutComps[i]["CmpNameEN"]] = nutritions[i+2]
	foods.append(food)
dkTab1.close()
print json.dumps(foods, sort_keys=True, indent=4)