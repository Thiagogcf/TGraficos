import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import matplotlib.ticker as tick


data = pd.read_csv('covid_19_data.csv')

plt.figure(figsize=(16, 9))
xa = range(len(data['SNo']))
xval = []
yval = []
xvala = []
yvala = []

def plotar(filtro,filtrado,vy):
    for i in range(len(data['SNo'])):
        if str(data[filtro][i]) == filtrado:
            yval.append(float(data[vy][i]))
            auxdata = datetime.strptime((data['ObservationDate'][i]), '%m/%d/%Y')
            xval.append(auxdata)

    plt.plot(xval, yval, label=filtrado)
    xval.clear()
    yval.clear()

# plt.ticklabel_format(axis="y",style='sci',scilimits=(0,0))
plotar('Province/State','Santa Catarina','Confirmed')
plotar('Province/State','Bahia','Confirmed')
plotar('Province/State','Rio de Janeiro','Confirmed')
plotar('Province/State','Rondonia','Confirmed')
plotar('Province/State','Parana','Confirmed')

# for i in range(len(data['SNo'])):
#     if str(data['Province/State'][i]) == 'Santa Catarina':
#         yval.append(float(data['Confirmed'][i]))
#         auxdata = datetime.strptime((data['ObservationDate'][i]), '%m/%d/%Y')
#         xval.append(auxdata)
# for i in range(len(data['SNo'])):
#     if str(data['Province/State'][i]) == 'Bahia':
#         yvala.append(float(data['Confirmed'][i]))
#         auxdata = datetime.strptime((data['ObservationDate'][i]), '%m/%d/%Y')
#         xvala.append(auxdata)
# x = range(len(xval))
# plt.plot(xval, yval, label = "line 1")
# plt.plot(xvala, yvala, label = "line 2")
# plt.locator_params(axis='y', nbins=10)
plt.legend()
# plt.show()
plt.savefig('1.png')
