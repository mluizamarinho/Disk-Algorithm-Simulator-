# algoritmo c-scan

# tempo de seek entre trilhas para mover o braço em ms
seek = 1.0

# tempo de rotação médio em ms para um disco com 7200 RPM
rotate = 4.5

# taxa de transferencia em MB/s
transfer = 54 

def pending_req(list):
  for c in list:
    if(c == 1):
      return True
  return False 

def last_req(list, aux):
    maior = 0
    i = 0 
    for c in range(len(list)):
        if(list[c] > maior and aux[c] != 0):
            maior = list[c]
            i = c
    return i    

def c_scan(requests, start):

    # ordenando a fila de requests (montando uma visão do disco)
    requests = sorted(requests)
    aux = [1] * len(requests)

    id = start 
    time = 0

    #tempo de seek para atender o primeiro é zero
    aux[id] = 0
    #calcula a posição da ultima requisição na direção em que a agulha esta indo
    last_request = last_req(requests, aux)
    while(pending_req(aux)):
        id += 1
        time += requests[id] - requests[id - 1]
        aux[id] = 0
        print(aux)
              
        if(id == len(requests) - 1 or id == last_request):
            time += requests[id] - requests[0]
            id = 0
            aux[id] = 0
    
    return time

requests = [98, 183, 37, 122, 14, 124]

# head começando na trilha mais interna
start = 3

const = c_scan(requests, start)

print("Tempo total:", const)
print("Tempo médio de resposta:", const/len(requests))