n, k = map(int, input().split())
# 랜선의 길이 담은 리스트
lan = [int(input()) for i in range(n)]
# 갖고 있는 랜선중 최대값
max_lan = max(lan)
# 후보군 담을 리스트
res = []

def binary(k, start, end):
	# 이분탐색 시작
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in lan:
        	# 구해진 값으로 랜선을 잘라본다
            cnt += i//mid
        # 자른 랜선들이 k 보다 작다면 좀더 작게 잘라야함
        if cnt < k: 
            end = mid - 1
        # 조건을 만족하는 경우.
        else:
        	# 후보에 넣고 좀더 크게 만들어봄
            res.append(mid)
            start = mid + 1
# 이분탐색 함수 호출
binary(k,1,max_lan)
# 후보군에서 최대값 출력
print(max(res))