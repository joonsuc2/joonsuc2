# function1.py

print('\033[43m' "---함수 정의---"   '\033[0m')
def setValue(newValue):
    x = newValue
    print("함수내부:", x)

print('\033[43m' "---함수 호출---"   '\033[0m')
retValue = setValue(5)
print(retValue)

print('\033[43m' "---함수 정의---"   '\033[0m')
def swap(x,y):
    return y,x

print('\033[43m' "---호출---"   '\033[0m')
result = swap(3,4)
print(result)
