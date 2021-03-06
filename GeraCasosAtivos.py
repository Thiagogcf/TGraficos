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
# filtraregioes()
# random.shuffle(regioes)
regioes = ["Rio de Janeiro","Quebec"]
for z in range(len(regioes)):
    plotar('Province/State', str(regioes[z]), 'Confirmed')
plt.legend()
plt.title("Comparação inverno e verão")
plt.ylabel("Casos Ativos")
plt.xlabel("Periodo")
# plt.show()
plt.savefig('Comparação inverno e verao.png')
