import os
import sys
import random
from mpi4py import MPI



os.system('clear')

#print('********************')
#print('** Mult Core **')
#print('********************')


comm = MPI.COMM_WORLD
rank = comm.Get_rank()

TAMANHO_MEDICAO = int(sys.argv[1])
TAMANHO_CORE = comm.Get_size()

soma_usuario = 10 #int(input('Qual a soma? '))
medicao = []
if rank == 0:
    medicao = random.sample(range(1, TAMANHO_MEDICAO+1), TAMANHO_MEDICAO) #input('Digite os valores (%d valores com espaços entre eles): ' %tam_medicoes).split(' ')
    for i in range(1, TAMANHO_CORE):
        comm.send(medicao, i)
    

else:
    medicao = comm.recv(source=0)

combinacoes0 = []
for i in range(int(rank*(((2**TAMANHO_MEDICAO)/TAMANHO_CORE)+1)), int((rank+1)*((2**TAMANHO_MEDICAO)/TAMANHO_CORE))):
    x = bin(i)  
    combinacoes0.append(x.split('b')[1].zfill(TAMANHO_MEDICAO))


total0 = 0
resultato_fatores = []
for l in combinacoes0:
    soma = 0
    fatores = list(l)
    for pos in range(0, len(l)):
        soma += int(fatores[pos]) * int(medicao[pos])
    if soma == soma_usuario:
        total0 += 1
        resultato_fatores.append(fatores)


if rank != 0:       
    #print("Enviando {}" .format(rank))
    comm.send(resultato_fatores, 0)        
    #print("Enviou {}" .format(rank)) 
else:
    for i in range(0, TAMANHO_CORE -1):
        resultato_fatores.append(comm.recv())
    
    #print(resultato_fatores)
