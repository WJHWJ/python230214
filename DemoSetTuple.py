# DemoSetTuple.py
tp = (1,2,3)
print( len(tp) )
print( tp[0] )

#함수 정의
def calc(a,b):
    return a+b, a*b

#함수 호출
result = calc(3,4)
print(result)
print(result[0])
print(result[1])
print(type(result))

print("id:%s, name:%s"%("kim","김유신"))

#set 연습
print("---set 연습---")
a = {1,2,3,3}
b = {3,4,5,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

print("---형식변환---")
b = set((1,2,3))
print( type(b) )
print( b )
c = list(b)
c.append(4)
print( c )

color = { "apple":"red", "banana":"yesllow"}
print( len(color) )
print( color["apple"] )
color["cherry"] = "red"
print(color)
del color["apple"]
print(color)

