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


def plotar(filtro,filtrado,vy):
    for i in range(datetime.strptime((data['ObservationDate'][i]))):
        if str(data[filtro][i]) == filtrado:
            yval.append(int(data[vy][i]))
            auxdata = datetime.strptime((data['ObservationDate'][i]), '%m/%d/%Y')
            xval.append(auxdata)

    plt.plot(xval, yval, label=filtrado)
    print(yval)
    xval.clear()
    yval.clear()

# plt.ticklabel_format(axis="y",style='sci',scilimits=(0,0))
plotar('Province/State','Santa Catarina','Confirmed')
# plotar('Province/State','Bahia','Confirmed')
plotar('Province/State','Rio de Janeiro','Confirmed')
# plotar('Province/State','Rondonia','Confirmed')
plotar('Province/State','Parana','Confirmed')
plotar('Province/State','Sao Paulo','Confirmed')
# ax = plt.gca()
# ax.set_ylim([0, 5000000])
plt.legend()
plt.show()
# plt.savefig('1.png')
