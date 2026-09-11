# 문자열(str)
# "", ''

a = "python"
print(a, type(a)) # python <class 'str'>

print("I'll be back.") #작은 따옴표가 있을 땐 반드시 큰 따옴표로 감싸야 함
print('I\'ll be back.') #역슬래시로 이스케이프 처리 가능

# 여러줄 문자열
a = """
Life is short
You need Python
"""
print(a)

def func():
    """
    func() 함수에 대한 설명
    """

print(func.__doc__) # func() 함수에 대한 설명

# 문자열 연결
print("Hello" + "Python") # HelloPython

# 문자열 반복
print("Hello" * 10) # Hello 10번 반복
print("-" * 20) # - 20번 반복

# 문자열 연산시 주의사항
# print("Hello" + 3) # TypeError: can only concatenate str (not "int") to str
print("Hello" + str(3)) # Hello3

print("10" + "2")
print(int("10") + int("2")) # 12

# 문자열 포맷팅 (f-string)

name = "뽀로로"
age = 23

print(f"이름: {name}, 나이: {age}") # 이름: 뽀로로, 나이:23
print(f"내년 나이: {age + 1}살") # 내년 나이:24살
print(f"{name.upper()}") # 뽀로로를 대문자로 출력 (영어만 가능)

pi = 3.141592653589793

print(f"{pi:.3f}") # 3.142
print(f"{pi:.0f}") # 3

num = 123456789
print(f"{num:,}") # 123,456,789

print(f"{num:15,d}") # 123,456,789 
print(f"{num:<15,d}") # 123,456,789

print(f"{num:015,d}") # 000,123,456,789
print(f"{num:<015,d}") # 123,456,78900000
