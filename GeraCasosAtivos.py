import random
import random

import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.ticker as tick
from matplotlib.ticker import MaxNLocator


data = pd.read_csv('covid_19_data.csv')

plt.figure(figsize=(16, 9))
xa = range(len(data['SNo']))
xval = []
yval = []
xvala = []
yvala = []
regioes= []
def filtraregioes():
    for i in range(len(data['ObservationDate'])):
        if str(data['Country/Region'][i]) == 'Brazil':
            if (str(data['Province/State'][i]) not in regioes) and (
                    str(data['Province/State'][i]) not in ('nan', 'Unknown')):
                regioes.append(str(data['Province/State'][i]))
    print(regioes)

def plotar(filtro,filtrado,vy):
    for i in range(len(data['ObservationDate'])):
        if str(data[filtro][i]) == filtrado:
            yval.append(int(data[vy][i])-int(data['Deaths'][i])-int(data['Recovered'][i]))
            auxdata = datetime.strptime((data['ObservationDate'][i]), '%m/%d/%Y')
            xval.append(auxdata)

    plt.plot(xval, yval, label=filtrado)
    print(yval)
    xval.clear()
    yval.clear()
filtraregioes()
random.shuffle(regioes)
for z in range(3):
    plotar('Province/State', str(regioes[z]), 'Confirmed')
# # plt.ticklabel_format(axis="y",style='sci',scilimits=(0,0))
# plotar('Province/State','Santa Catarina','Confirmed')
# # plotar('Province/State','Bahia','Confirmed')
# plotar('Province/State','Rio de Janeiro','Confirmed')
# # plotar('Province/State','Rondonia','Confirmed')
# plotar('Province/State','Parana','Confirmed')
# plotar('Province/State','Sao Paulo','Confirmed')
plt.legend()
plt.show()
# plt.savefig('1.png')
