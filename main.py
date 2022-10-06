from asyncio.windows_events import NULL
from random import *
import matplotlib.pyplot as plt

## CONFIGURAÇÕES

TAMANHO = 100
ALTURA = (0, 10)

##################

listaX = []
listaY = []

for i in range(TAMANHO):
    if randint(0,100) <= 80 and len(listaY) > 0:
        y = listaY[-1]
    elif randint(0,100) <= 90:
        pass
    else:
        y = randint(ALTURA[0], ALTURA[1])
    listaX.append(i)
    listaY.append(y)
    print(y)

plt.plot(listaX, listaY)
plt.show()