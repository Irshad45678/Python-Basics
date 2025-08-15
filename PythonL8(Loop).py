#11. Loops

#For loop

for i in range(5):
    print(i)

for item in ["a","b","c"]:
    print(item)


#While loop

count = 0
while count < 5:
    print(count)
    count += 1


#Break & Continue

for i in range(5):
    if i == 3:
        break
    if i == 1:
        continue
    print(i)