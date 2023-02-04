for x in range(151):
    print(x)

for i in range(100):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)


count = 0
for i in range(1, 500000):
    if i % 2 != 0:
        count += i
print("Hay", count, "si se suman todos los impares hasta el 500000")

i=0
for i in range (2018,0,-4):
    print(i)


print("opcional---------------------------------------")

lowNum = 2
highNum = 9
mult = 3

for a in range(lowNum,highNum,1):
    if a % mult == 0:
        print(a)