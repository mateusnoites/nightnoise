from asyncio.windows_events import NULL
from random import *
import matplotlib.pyplot as plt

## CONFIGURAÇÕES

TAMANHO = 64
ALTURA = (0, 10)

##################

listaX = []
listaY = []

for i in range(TAMANHO):
    if listaY == "SUBSTITUI!!":
        pass
    y = randint(ALTURA[0], ALTURA[1])
    listaX.append(i)
    listaY.append(y)
    print(y)


plt.plot(listaX, listaY)
plt.show()