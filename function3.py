# function3.py

# 정의되지 않은 인자 (딕셔너리)
print('\033[43m' "---정의되지 않은 인자 (딕셔너리)---"   '\033[0m')  
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():  #딕셔너리는 기정의된 메서드 : items(), keys(), values()
        strURL += key + "=" + user[key] + "&"
    return strURL

# 호출
print(userURIBuilder("ycampus.com","80",id="kim",pwd="1234"))
print(userURIBuilder("ycampus.com","80",id="kim",pwd="1234",  \  
 name="mike", age="30"))  # \ --> 다음줄로 넘어감

