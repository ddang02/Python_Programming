# for문

# for (int i = 0; i < 10; i++)  # C언어
# for i in iterable객체:        # Python

for i in range(5):  # == for i in range(0, 5)
    print(i, end=" ")
print()

a = range(5)
print(a.start, a.stop, a.step)  # 시작이 0

# 1 ~ 5까지
for i in range(1, 6):
    print(i, end=" ")
print()

# 0 ~ 10 중에 짝수 출력
for i in range(0, 11, 2):
    print(i, end=" ")
print()

# 5 4 3 2 1 거꾸로 출력
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# 1 ~ 10까지의 합
tot = 0
for i in range(11):
    tot += i
print(tot)

# 1 ~ 10까지의 합
print(sum(range(1, 11)))
print()

# 문자열 반복 출력
s = "ab12!@한글韓自🥵"
for c in s:
    print(c, end=" ")
print()

print(len(s))

# 구구단 출력
# 2 * 1 = 2 2 * 2 = 4 ... 2 * 9 = 18

for i in range(1, 9, 1):
    i += 1
    for j in range(9):
        j += 1
        print(f"{i} * {j} = {i * j:<5d}", end="")
