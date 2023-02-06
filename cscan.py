# algoritmo c-scan

# tempo de seek entre trilhas para mover o braço em ms
seek = 1.0

# tempo de rotação médio em ms para um disco com 7200 RPM
rotate = 4.5

# taxa de transferencia em MB/s
transfer = 54 

def pending_rq(list):
  for c in list:
    if(c == 1):
      return True
  return False 

def c_scan(requests, start):

    # ordenando a fila de requests (montando uma visão do disco)
    requests = sorted(requests)
    aux = [1] * len(requests)

    id = start 
    time = 0

    #tempo de seek para atender o primeiro é zero
    aux[id] = 0
  
    while(pending_rq(aux)):
        id += 1
        time += requests[id] - requests[id - 1]
        aux[id] = 0
              
        if(id == len(requests) - 1 or aux[id + 1] == 0):
            time += requests[id] - requests[0]
            id = 0
            aux[id] = 0
    
    return time

requests = [98, 183, 37, 122, 14, 124]

# head começando na trilha mais interna
start = 0

const = c_scan(requests, start)

print("Tempo total:", const)
print("Tempo médio de resposta:", const/len(requests))