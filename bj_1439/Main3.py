import sys

s = list(sys.stdin.readline().rstrip())
s = list(map(int, s))  # 문자열 '0' -> 0으로, '1'을 1로 변환

zero_result = 0  # 0을 뒤집었을 경우
one_result = 0  # 1을 뒤집었을 경우

for i in range(len(s) - 1):
  if s[i] == 1:  # 뒤집어야 하는게 1인 경우
    if s[i + 1] != 1:  # 현재 값은 1이 아니다. -> 연속적인게 끝났다. -> 값을 증가
      one_result += 1
  else:  # 뒤집어야 하는게 0인 경우
    if s[i + 1] != 0:
      zero_result += 1

# 마지막 문자 계산
if s[-1] == 0: 
  zero_result += 1
else:
  one_result += 1

# 0을 뒤집었을 때, 1을 뒤집었을 때 중에서 최소값을 출력
print(min(one_result, zero_result))