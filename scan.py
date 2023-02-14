# -*- coding: utf-8 -*-

import random
# O disco tem 25 trilhas e 1 setor

disk = []

for d in range(25):
    disk.append(-1)



# tempo de seek entre trilhas para mover o braço em ms

seek_time = 1.0


#requisições de escrita

write_requests = [2, 10, 8, 5, 17, 4, 23, 1, 7, 12]


aux_requests = sorted(write_requests)


# Escolhe uma posição para a agulha começar

start_value = random.randint(0,24)


def scan():

    index_start = binary_search(start_value, aux_requests)
    curr = start_value
    time = 0

    seek = 0

    # do start para a esqerda

    for i in range(index_start, -1, -1):
        seek += curr - aux_requests[i]
        time += seek * 1
        curr = aux_requests[i]
        disk[curr] = curr

    #da esquerda para direita

    for j in range(index_start+1, len(aux_requests)):
        seek += aux_requests[j] - curr
        time += seek * 1
        curr = aux_requests[j]
        disk[curr] = curr

    return seek



#verifica índice do maior número que é menor ou igual ao valor inicial da agulha

def binary_search(start, requests):
    i = 0
    l = len(requests)-1
    ans = 0
    while i <= l:
        mid = (i+l) // 2
        if (requests[mid] <= start):
            ans = mid
            i = mid + 1
        else:
            l = mid - 1
    return ans


if __name__ == '__main__':
    v = scan()


print("Start position: " + str(start_value))
print("Requests: " + str(write_requests))
print("Seek time: " + str(v))
print("Average seek time: " + str(v/len(aux_requests)))
print("Disk after requests: " + str(disk))