from cProfile import label
from xml.dom.minidom import TypeInfo
import matplotlib.pyplot as plt
import pandas as pd

dadosSingle = pd.read_csv('saidaSigleCore.dat', sep=';', header=None)

dadosMulti = pd.read_csv('saidaParalelo.dat', sep=';', header=None)

listDadosSingle = dadosSingle.values.tolist()
listDadosMulti = dadosMulti.values.tolist()

razaoDados = []

for i in range(0, len(listDadosSingle)):
    razao_aux = []
    razao = listDadosSingle[i][1] / listDadosMulti[i][1]

    razao_aux.append(listDadosSingle[i][0])
    razao_aux.append(round(razao, 2))
    razaoDados.append(razao_aux)

razatDt = pd.DataFrame(razaoDados, columns=[0, 1])

plt.subplot(1, 2, 1)
plt.plot(dadosSingle[0], dadosSingle[1], ls='-', lw='1', marker='o', label='SingleCore')
plt.plot(dadosMulti[0], dadosMulti[1], ls='-', lw='1', marker='o', label='MultiCore')
plt.title('Diferença de tempo SingleCore/MultiCore')
plt.grid()
plt.legend(loc="upper left")

plt.subplot(1, 2, 2)
plt.plot(razatDt[0], razatDt[1], ls='-', lw='1', marker='o', label='Razão das medições')
plt.title('Razao dos tempos')
plt.grid()
plt.legend(loc="upper left")
plt.show()