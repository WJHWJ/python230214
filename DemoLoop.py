# DemoLoop.py

for i in [2,3,4,5,6]:
    print("-----{0}단-----".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))


print("---break---")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("item:{0}".format(i))

print("---continue---")
lst = [1,2,3,4,5,6,7,8,9,10]
#디버깅할 때 중단점(Break Point)
for i in lst:
    if i % 2 == 0:
        continue
    print("item:{0}".format(i))

print("---수열함수---")
print(list(range(10)))
print(list(range(0,11)))
print(list(range(10,0,-1)))

years = list(range(2000,2024))
print(years)
print(list(range(1,32)))

print("---수동루프---")
for i in range(10):
    print(i)

print("---리스트 컴프리헨션---")
lst = list(range(1,11))
print( [i**2 for i in lst if i>5] )

d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()] )

print("---필터링--")
lst = [10,25,30]
iterL = filter(None, lst)
for i in iterL:
    print (i)

print("---함수로 필터링--")
def getBiggerThan20(i):
    return i>20

lst = [10,25,30]
iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print (i)