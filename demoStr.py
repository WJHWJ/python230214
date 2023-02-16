# demoStr.py
s = "abcdef"
print(s[:2])
print(s[-2:])
print(len(s))

#특수문자(탈출문자)
print("c:\work\test.txt")
print("c:\\work\\test.txt")
#raw string notation(가공하지 않은 문자열): 소문자 r
print(r"c:\work\test.txt")

#파일 저장
f = open("c:\\work\\data.txt","wt",encoding="utf-8")
names = ["김길동","홍길동","전우치"]
for name in names:
    f.write("안녕하세요 {0}님 봄입니다!".format(name) + "\n")
    f.write("=" * 40)
    f.write("\n")
f.close()

#str클래스의 메서드
#print(dir(str))
strA = "python is powerful"
strB = "파이썬은 강력해"
print( strA.capitalize() )
print( strA.upper() )
print( len(strA) )
print( len(strB) )
print("---알파벳과 숫자로만 구성---")
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isnumeric())

#문자열을 가공(전처리)
u = "<<<  spam is ham  >>>"
result = u.strip("<> ")
print(u)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
lst = result2.split()
print(lst)
print(":)".join(lst))
print(lst)