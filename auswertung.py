import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----- load data ---------
confirmed_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
help(pd.DataFrame.groupby)
confirmed = confirmed_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])
deaths = deaths_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])


# ------ plot evolution of cases ------
countries = ['Germany', 'Italy', 'Spain', 'France']
fig = plt.figure()
for i, country in enumerate(countries):
    fig.add_subplot()
