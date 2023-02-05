import random
import time 
# The disk have 50 trails and 1 sector

disk = []

for d in range(50):
    disk.append(-1)
print(disk)

# The disk is empty


write_requests = [2,10,8,5,33,28,17,4,23,1,7,49,41,36,12]

aux_requests = sorted(write_requests)

start_value = random.randint(0,49)

def scan():

    start_value = random.randint(0,49)

    index_start = binary_search(start_value, aux_requests)

    curr = start_value

    seek = 0

    for i in range(index_start,-1,-1):
        seek += curr - aux_requests[i]
        curr = aux_requests[i]
        disk[curr] = curr

    for j in range(index_start+1,len(aux_requests)):
        seek += aux_requests[j] - curr
        curr = aux_requests[j]
        disk[curr] = curr


def binary_search(start, requests):
    i = 0
    l = len(requests)-1
    ans = 0
    while i <= l:
        mid = (i+l) // 2
        if(requests[mid] <= start):
            ans = mid
            i = mid + 1
        else:
            l = mid - 1
    return ans


