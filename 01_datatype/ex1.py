# 변수
a = 2
b = 3
print(a, b)  # 2 3

# a = 2, b = 3 -> a = (2, b) = 3 error
a = 2; b = 3
a, b = 2, 3 #권장
print

# 값 swap
temp = a
a = b
b = temp
print(a, b)  # 3 2

a, b = b, a
print(a, b)  # 2 3

# 변수명 규칙 (C와 동일)
# 1. 알파벳, 숫자, 밑줄(_)만 사용 가능
# 2. 숫자로 시작할 수 없음
# 3. 예약어는 사용할 수 없음
# 4. 대소문자 구분함

# name! = "뽀로로" #특수문자 사용 불가
# 2name = "크롱" #숫자로 시작 불가
# _age = 16 _사용 가능
# class = "루피"  # 예약어 사용 불가
이름 = "또유니"  # 한글 변수명 가능
print(이름)  # 또유니

student_name = "또유니"  # snake_case
studentName = "또유니"  # camelCase

MAX_SCORE = 100  # 상수는 대문자 사용 권장
