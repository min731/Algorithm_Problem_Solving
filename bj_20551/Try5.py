def lower_bound(array,target):

    left , right = 0, len(array)-1
    
    while left<=right:

        mid = (left+right)/2

        if array[mid] >= target:
            right = mid
        else:
            left = mid+1

    try:
        if array[left] == target:
            return left
        else:
            return -1
    except:
        return -1
    
lower_bound([1,2,3,4,5],4)