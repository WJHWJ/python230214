# class2.py
#1) 클래스 정의
class Person:
    #클래스 멤버변수
    num_person = 0
    #초기화 메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print( "My name is {0}.".format(self.name) )

#2) 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print( "인스턴스 갯수:{0}".format(Person.num_person) )

p1.age = 30
print(p1.age)
#print(p2.age)

