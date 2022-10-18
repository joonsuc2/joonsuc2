# demoDict.py
color = {"apple":"red", "banana":"yellow"}
print(color)
print(len(color)) # 방의 갯수 (애플방, 바나나방)
print(color["apple"])
color["kiwi"]="green" # 추가
print(color)

# 반복문
print('\033[43m'"---반복문---"'\033[0m')
for item in color.items():
    print(item)

for k,v in color.items():
    print(k,v)

print('\033[43m' "---device---"   '\033[0m')
device = {"아이폰":5, "아이패드":10, "타블렛":20}
print(device["아이폰"])
device["맥북"] = 15
print(device)
device["아이폰"]=6
del device["타블렛"]
print(device)

print('\033[43m' "---참조만 복사---"   '\033[0m')
phone = {"kim":"111","lee":"222","park":"333"}
print(phone["kim"])
print("kim" in phone)
print("kang" not in phone)

print('\033[43m' "---복사 기능---"   '\033[0m')
p=phone
p["kang"]="123"
print(phone)
print(p)
print(id(phone), id(p)) #메모리 구조에 따라 숫자는 변경되나, phone과 p 숫자 일치함

print('\033[43m' "---같은지 아닌지 비교---"   '\033[0m')
if(id(phone)==id(p)):
    print("true")
else:
    print("false")





