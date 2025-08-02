n, m = map(int, input().split())
array = list(map(int, input().split()))

def solution(array, m):
    start = 0
    end = max(array)
    result = 0  # 최적 높이 저장

    while start <= end:
        mid = (start + end) // 2  # 자를 높이
        total = 0

        # mid 높이로 잘랐을 때 잘려나가는 총합 계산
        for tree in array:
            if tree > mid:
                total += tree - mid

        if total >= m:
            # 잘린 양이 충분함 → 더 높이 자를 수 있을지도?
            result = mid         # 현재 높이는 유효
            start = mid + 1      # 더 높은 범위 탐색
        else:
            # 부족함 → 너무 높게 잘랐다
            end = mid - 1        # 더 낮은 범위 탐색

    return result

print(solution(array, m))