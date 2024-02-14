from collections import deque,Counter
from itertools import chain

def box_sum(box):
    # print(box)
    # print(list(chain(*box)))
    return sum(list(chain(*box)))

def get_boxes(new_arr):

    length = len(new_arr[0])
    box1 = [subarr[:length//2] for subarr in new_arr[:length//2]]
    box2 = [subarr[:length//2] for subarr in new_arr[length//2:length]]
    box3 = [subarr[length//2:length] for subarr in new_arr[:length//2]]
    box4 = [subarr[length//2:length] for subarr in new_arr[length//2:length]]
    boxes = [box1, box2, box3, box4]
    
    return boxes

def solution(arr):
    answer = [0,0]
    
    arr_sum = box_sum(arr)
    if arr_sum==0:
        return [1,0]
    elif arr_sum==len(arr)**2:
        return [0,1]
    
    queue = deque([arr])
    
    while queue:
        
        new_arr = queue.popleft()
        boxes = get_boxes(new_arr)
        
        for box in boxes:
            length = len(box) 

            sum_box = box_sum(box)
            
            if box:
                if sum_box==0:
                    answer[0] += 1
                elif sum_box==length**2:
                    answer[1] += 1

                else:
                    queue.append(box)

    return answer