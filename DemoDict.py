# DemoDict.py
device = { "아이폰":5, "아이패드":10, "윈도우":20 }
print( device["아이폰"] )
device["맥"] = 15
print( device )

device["아이폰"] = 6
del device["맥"]
print ( device )

print("---명함관리---")
phone = {"kim":"1111", "lee":"2222", "park":"3333"}
print ( "kim" in phone )
print ( "moon" in phone )
print ( "moon" not in phone )

for item in phone.items():
    print(item)

for k,v in phone.items():
    print(k, v)

print("---keys()---")
for k in phone.keys():
    print(k)

print("---values()---")
for v in phone.values():
    print(v)

print("참조를 전달")
p = phone
phone["moon"] = "1234"
print( phone )
print( p )
print( id(phone), id(p) )

a = [1,2,3]
b = a
a[0] = 38
print(a)
print(b)
print( id(a),id(b) )

print("---deep copy---")
a = [1,2,3]
b = a[:]
a[0] = 38
print(a)
print(b)
print( id(a),id(b) )

import copy
a = [100,200,300]
b = copy.deepcopy(a)
a[0]=101
print(a)
print(b)
print( id(a),id(b) )

isRight = True
print( type(isRight) )
print( 1 < 2 )
print( 1 == 2 )
print( 1 != 2 )
print( True and True and True )
print( True and True and False )
print( True or False or False )