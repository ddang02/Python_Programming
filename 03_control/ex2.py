# 반복문: while문, for문

# while문
# 1 ~ 10까지 반복 출력
i = 0
while i < 10:
    i += 1
    print(i)
    # if i == 5:  #while문 안에서 if문 사용 가능
    #     break
else:
    print("End")

nums = [1, 3, 5, 7, 9]
target = 2
i = 0

while i < len(nums):
    if nums[i] == target:
        print(f"{target} found")
        break
    i += 1
else:
    print(f"{target} not found")

# 1 ~ 10까지의 합
# sum = 55
i = 1
tot = 0
while i <= 10:
    tot += i
    i += 1
print(f"sum = {tot}")

# 1 ~ 10 사이 홀수의 합
# sum = 30
i = 1
tot = 0

while i <= 10:
    if (i % 2) == 1:
        pass
    else:
        tot += i
    i += 1
print(f"sum = {tot}")
