# 객체 조사를 위한 함수
#1. dir()
"""
인자로 전달된 객체가 가지고 있는 변수, 메서드와 같은
속성정보를 리스트 객체로 반환.
인자를 전달하지 않고 호출하면 현재 지역 스코프에 대한 정보를 리스트 객체로 반환
"""
###

# 2. globals() locals()
"""
현재의 전역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수
(전역변수와 함수, 클래스의 정보 포함)

현재 지역 심볼 테이블을 보여주는 딕셔너리를 반환하는 함수
(매개변수를 포함한 지역변수와 중첩함수의 정보 포함)
"""

# id() 변수의 메모리 주소값을 반환함
# ininstance(), issubclass() 딱봐도 뭔지 안다.
# eval() 실행가능한 문자열 변수를 실행시킴.


data_list = list(range(1, 21))

map_list = list(map(lambda x : x + 5, data_list))
filter_list = list(filter(lambda x : x % 3 == 0, map_list))

print("map_list = {0}".format(map_list))
print("filter_list = {0}".format(filter_list))
