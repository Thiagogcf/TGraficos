import pandas as pd

data = pd.read_csv('covid_19_data.csv')
regioes = []
for i in range(len(data['ObservationDate'])):
    if  str(data['Country/Region'][i]) == 'Brazil':
        if (str(data['Province/State'][i]) not in regioes) and (str(data['Province/State'][i]) not in ('nan','Unknown')):
            regioes.append(str(data['Province/State'][i]))
print(regioes)