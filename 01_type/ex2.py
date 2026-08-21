# 파이썬 자료형
# 1. 기본 자료형: 숫자형(정수형, 실수형), 불리언, 문자열
# 2. 컬렉션 자료형: 리스트, 튜플, 딕셔너리, 집합

# 숫자형 - 정수형(int)
a = 10
print(a, type(a))  # 10 <class 'int'>

# 2진수, 8진수, 16진수
print(bin(a), oct(a), hex(a))  # 0b1010 0o12 0xa
print(ord("A"), chr(65))  # 65 A

# int 데이터의 표현 범위
x = 10**100  # 10의 100제곱
print(x)

# 오버플로우 테스트
a = 2**31 - 1
print(a)
a = a + 1  # C의 경우 오버플로우 발생
print(a)

# 숫자형 - 실수형(float)
b = 3.14
print(b, type(b))  # 3.14 <class 'float'>

# float의 표현 범위
# 부동소수점 방식
# 64비트 = 부호(1비트) + 지수부(11비트) + 가수부(52비트)

import sys

print(sys.float_info.min)  # float의 최솟값
print(sys.float_info.max)  # float의 최댓값

print(-sys.float_info.min)  # float의 최솟값 음수
print(-sys.float_info.max)  # float의 최댓값 음수

a = 1.7e308
b = 1.8e308
print(a, b)  # 1.7e+308 inf

# 실수의 오차
print(0.1 + 0.2 == 0.3)  # False
print(f"{0.1:.20f}")
print(f"{0.2:.20f}")
print(f"{0.3:.20f}")

# 형변환
print(float(10))  # 10.0
print(int(3.14))  # 3
print(int("100"))  # 100
print(float("3.14"))  # 3.14
