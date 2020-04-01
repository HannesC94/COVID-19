import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%----- load data --------
confirmed_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
confirmed = confirmed_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])
deaths = deaths_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])

# %% ------ plot evolution of cases ------
countries = ['Germany', 'Italy', 'Spain', 'France', 'US', 'United Kingdom']
fig, ax = plt.subplots(1)
for i, country in enumerate(countries):
    days = confirmed.loc[country].index[-30:]
    cases = confirmed.loc[country].values[-30:]
    ax.plot(days, np.log(cases), label=countries[i])
    # ax.xaxis.x
plt.legend()
plt.show()

# %% ------- display deaths and cofirmed cases
start_date =
