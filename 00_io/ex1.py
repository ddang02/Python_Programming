# 입출력

a = input()
print(a, end="")
print(type(a))  # str
print(a, type(a), sep=", ")  # sep: 구분자

a = int(a)
print(a, type(a))

a = int(input())
print(a, type(a))

b = float(input())
print(b, type(b))

# 정수 2개 입력
# 100
# 200
a = int(input())
b = int(input())
print(a, b)

a = input().split()  # 공백 기준으로 나눠서 리스트로 반환
print(a, type(a))  # ['100', '200'] <class 'list'>

# map
# map(함수, List 객체) : 반복 가능한 자료형의 각 요소를 함수로 처리해주는 함수
a, b, c = map(int, input().split())
print(a, b, c)

# 리스트 변환
a = list(map(int, input().split()))  # [100, 200, 300]
print(a, type(a))
