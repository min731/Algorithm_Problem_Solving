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

    if len(arr)==1:
        if arr[0][0]==0:
            return [1,0]
        else:
            return [0,1]
        
    answer = [0,0]
    queue = deque([arr])
    
    # 출력
    for i in range(len(arr)):
        print(arr[i])
    
    while queue:
        print("---------------------------------------------------------")
        
        new_arr = queue.popleft()
        boxes = get_boxes(new_arr)
        
        for box in boxes:
            length = len(box)

            print("--------box!--------")
            for i in range(len(box)):
                print(box[i])
            print("length : ",length)

            # if len(box)==1:
            #     box_cnt = Counter(list(chain(*box)))
            #     answer[0] += box_cnt[0] 
            #     answer[1] += box_cnt[1] 

            sum_box = box_sum(box)
            
            if box:
                if sum_box==0:
                    answer[0] += 1
                    print("0찾음!")
                elif sum_box==length**2:
                    answer[1] += 1
                    print("1찾음!")

                else:
                    # queue.append([subarr[:length//2] for subarr in box[:length//2]])
                    # queue.append([subarr[:length//2] for subarr in box[length//2:length]])
                    # queue.append([subarr[length//2:length] for subarr in box[:length//2]])
                    # queue.append([subarr[length//2:length] for subarr in box[length//2:length]])
                    queue.append(box)
                    # queue.append([subarr[:length//2] for subarr in box[length//2:length]])
                    # queue.append([subarr[length//2:length] for subarr in box[:length//2]])
                    # queue.append([subarr[length//2:length] for subarr in box[length//2:length]])
            print("--------box!--------")
        
    print(answer)
    return answer

# solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]])
# solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]])
solution([[1]])