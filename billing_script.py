import csv
import math


#initialize convert csv columns to rows
i = []
m = []
tot = 0
with open('bill.csv', 'rb') as f:
    for row in csv.reader(f, delimiter=','):
        i.append(row[0])
        m.append(row[1])

#determine machine types

n = ['8-standard-rings']
a = 0
slices = [0]

while a < len(i):
    if i[a] != n[(len(n)-1)]:
        n.append(i[a])
        slices.append(a)
        a = a+1
    else:
        a = a+1

slices.append(len(i))


#sum the minutes each task ran by machine-resource type

c = []

tot = 0
j = 1

for h in range(0, len(m)):
    if h != slices[j]:
        tot = tot + float(m[h])
    elif h == slices[j]:
        c.append(tot)
        tot = 0
        j = j + 1
        tot = tot + float(m[h])

#Convert to Hours

hours = []

for l in c:
    hours.append(l/3600)

for d in range(len(hours)):
    print(str(n[d]) + ":" + str(hours[d]))
