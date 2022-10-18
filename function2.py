# function2.py

#함수정의

def change(x):
    x[0]="H"

#함수 호출
worldlist = ["J", "A", "M"]
print(worldlist)
change(worldlist)
print("함수호출후: ",worldlist)

# Deep Copy
print('\033[43m' "---Deep Copy---"   '\033[0m')    
def change(x):
    #전체복사
    x1 = x[:]
    x1[0] = "H"
    print ("함수내부: ",x1)
print('\033[43m' "---함수 호출---"   '\033[0m')
worldlist = ["J", "A", "M"]
change(worldlist)
print("함수호출후: ",worldlist)

# 전역변수 지역변수
print('\033[43m' "---전역변수 지역변수---"   '\033[0m')  
x = 2
def func1(a):
    return a+x

print(func1(1))

def func2(a):
    x=2
    return a+x
print (func2(5))

# 디버깅 연습 예제 (교집합 가져오기)
print('\033[43m' "---디버깅 연습 예제---"   '\033[0m')  
def intersect(preslist, postlist):
    result = []  #비어있는 리스트 (교집합을 담을 리스트)
    for x in preslist: 
        if x in postlist and x not in result: #특정 글자가 postlist에 있고 x 가 result에 없으면
            result.append(x)
    return result
print(intersect("HAM","SPAM"))


# 기본값 명시
print('\033[43m' "---기본값 명시---"   '\033[0m') 
def times(a=10,b=20):
    return a*b

#호출
print(times()) # 10*20
print(times(5)) # 5*20
print(times(5,6)) # 5*6
print(times(b=10)) # 10*10

# 키워드 인자
print('\033[43m' "---키워드인자---"   '\033[0m') 
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL
print(connectURI("ycampus.com","80"))
print(connectURI(port="8080",server="ycampus.com"))

# 가변인자(입력 파라메터가 갯수가 가변적
print('\033[43m' "---가변인자---"   '\033[0m') 
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result :
                result.append(x)
    return result

print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))
