# Python 알고리즘 코딩테스트 자주 쓰는 라이브러리/함수 정리

> **손코딩 시험 직전, 빠르게 훑어보는 실전 예시 & 주석 모음**

---

## 1. 입력 빠르게 받기 (sys.stdin.readline)
```python
import sys
input = sys.stdin.readline
n = int(input())  # 예) 입력: 5\n → n = 5
```

## 2. 리스트 입력 한 줄에 받기
```python
arr = list(map(int, input().split()))  # 입력: 1 2 3 4 → arr = [1, 2, 3, 4]
```

## 3. 2차원 리스트 입력
```python
matrix = [list(map(int, input().split())) for _ in range(2)]  # 입력: 1 2 3\n4 5 6 → matrix = [[1,2,3],[4,5,6]]
```

## 4. collections.deque (양방향 큐)
```python
from collections import deque
q = deque([1,2,3])         # q = deque([1,2,3])
q.append(4)                # q = deque([1,2,3,4])
q.appendleft(0)            # q = deque([0,1,2,3,4])
q.popleft()                # 0 반환, q = deque([1,2,3,4])
q.pop()                    # 4 반환, q = deque([1,2,3])
```

## 5. collections.Counter (빈도수 세기)
```python
from collections import Counter
c = Counter([1,2,2,3,3,3]) # c = Counter({3: 3, 2: 2, 1: 1})
c.most_common(1)           # [(3, 3)]
```

## 6. heapq (최소/최대 힙)
```python
import heapq
h = []
heapq.heappush(h, 3)       # h = [3]
heapq.heappush(h, 1)       # h = [1,3]
heapq.heappush(h, 2)       # h = [1,3,2]
heapq.heappop(h)           # 1 반환, h = [2,3]
# 최대힙: heapq.heappush(h, -x), heapq.heappop(h)*-1
```

## 7. bisect (이진탐색, 정렬리스트 삽입/탐색)
```python
from bisect import bisect_left, bisect_right
arr = [1,2,2,2,3,4]
bisect_left(arr, 2)   # 1 (2가 처음 등장하는 인덱스)
bisect_right(arr, 2)  # 4 (2가 끝나는 다음 인덱스)
```

## 8. itertools (조합, 순열, 곱집합)
```python
from itertools import combinations, permutations, product
# 조합(combinations): 순서 상관없이 n개 중 r개 뽑기
for comb in combinations([1,2,3], 2):
    print(comb)
# (1, 2)
# (1, 3)
# (2, 3)

# 순열(permutations): 순서 있게 n개 중 r개 뽑기
for perm in permutations([1,2,3], 2):
    print(perm)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)

# 곱집합(product): 모든 조합 (중복 허용, 데카르트 곱)
for prod in product([0,1], repeat=2):
    print(prod)
# (0, 0)
# (0, 1)
# (1, 0)
# (1, 1)
```

## 9. math (수학 함수)
```python
import math
math.ceil(3.2)    # 4 (올림)
math.floor(3.7)   # 3 (내림)
math.gcd(12, 18)  # 6 (최대공약수)
math.lcm(12, 18)  # 36 (최소공배수, Python 3.9+)
math.inf          # 무한대
```

## 10. enumerate (인덱스와 값 동시 접근)
```python
arr = ['a', 'b', 'c']
for idx, val in enumerate(arr):
    print(idx, val)  # 0 a, 1 b, 2 c
```

## 11. zip (여러 리스트 동시 순회)
```python
for a, b in zip([1,2,3], [4,5,6]):
    print(a, b)  # 1 4, 2 5, 3 6
```

## 12. set (중복 제거, 집합 연산)
```python
s = set([1,2,2,3])   # s = {1, 2, 3}
s1 = {1,2,3}; s2 = {2,3,4}
s1 | s2  # {1,2,3,4} (합집합)
s1 & s2  # {2,3} (교집합)
s1 - s2  # {1} (차집합)
```

## 13. defaultdict (기본값 딕셔너리)
```python
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1           # d = {'a': 1}
```

## 14. lambda (간단한 익명함수)
```python
f = lambda x: x+1
f(2)  # 3
```

## 15. sorted (정렬, key 활용)
```python
arr = [(1,2), (3,1), (2,3)]
sorted_arr = sorted(arr, key=lambda x: x[1])  # sorted_arr = [(3,1), (1,2), (2,3)]
```

## 16. map, filter, reduce
```python
arr = ['1', '2', '3']
nums = list(map(int, arr))  # nums = [1, 2, 3]
evens = list(filter(lambda x: x%2==0, [1,2,3,4]))  # evens = [2,4]
from functools import reduce
reduce(lambda x, y: x+y, [1,2,3,4])  # 10
```

## 17. 문자열 관련 함수
```python
s = 'abcde'
s[::-1]                # 'edcba' (역순)
s.upper()              # 'ABCDE'
s.lower()              # 'abcde'
s.count('a')           # 1 ('a'의 개수)
s.find('b')            # 1 ('b'의 인덱스)
' '.join(['a','b','c'])         # 'a b c' (리스트를 문자열로 합침)
','.join(map(str, [1,2,3]))     # '1,2,3' (숫자 리스트를 문자열로)
```

## 18. 리스트 관련 함수
```python
arr = [1,2,3]
arr.append(4)          # arr = [1,2,3,4]
arr.pop()              # 4, arr = [1,2,3]
arr.insert(1, 5)       # arr = [1,5,2,3]
arr.remove(2)          # arr = [1,5,3]
arr.sort()             # arr = [1,3,5]
arr.reverse()          # arr = [5,3,1]
```

## 19. 2차원 리스트 전치 (transpose)
```python
matrix = [[1,2,3],[4,5,6]]
transposed = list(map(list, zip(*matrix)))  # transposed = [[1,4],[2,5],[3,6]]
```

## 20. 최대/최소값 구하기
```python
arr = [1,2,3]
max(arr)  # 3
min(arr)  # 1
```

## 21. any, all (하나라도/모두 True)
```python
arr = [0, 1, 2]
any(arr)  # True (하나라도 True)
all(arr)  # False (모두 True여야 True)
```

---

> **자주 쓰는 변수명/패턴**
- `arr`, `nums`, `matrix`, `graph`, `visited`, `queue`, `stack`, `answer`, `result`, `cnt`, `idx`, `n`, `m`, `k`, `x`, `y`
- BFS/DFS: `queue = deque([시작점])`, `stack = [시작점]`, `visited = [False]*n`
- 이진탐색: `start, end = 0, len(arr)-1`
- 정렬: `arr.sort()`, `sorted(arr, key=...)`

---

> **실전에서 자주 실수하는 부분**
- `input()`은 문자열, `map(int, input().split())`로 변환 필요
- `sys.stdin.readline()`은 개행문자 포함, `rstrip()`으로 제거
- heapq 최대힙은 음수로 push/pop
- bisect는 정렬된 리스트에서만 사용 가능
- Counter, defaultdict은 import 위치 주의

---

> **이 파일을 손코딩 시험 직전 꼭 한번 읽고 가세요!**
