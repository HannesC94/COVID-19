import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# %%----- load data --------
confirmed_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
deaths_series = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
# group by countries
confirmed = confirmed_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])
deaths = deaths_series.groupby('Country/Region').sum().drop(columns=['Lat', 'Long'])
death_rate = (deaths/confirmed).replace([np.inf], np.nan)
us = confirmed.loc['US']
us
inf = death_rate.loc['Vietnam', '1/23/20']
death_rate.loc[['Germany', 'US', 'Italy', 'Spain'], '4/7/20'].sort_values()

# %% evaluate USA
us = pd.read_csv(
    'csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_US.csv')
us[us['Province_State'].str.startswith('New')]
us_by_state = us.groupby(by='Province_State', as_index=True).sum()
us_by_state

# look at New York
ny = us_by_state.loc['New York', '2/20/20':'4/7/20']
plt.plot(ny.index, ny.values, label='NY')
plt.plot(deaths.loc['Italy', '2/20/20':'4/7/20'], label='italy')
plt.legend()
plt.show()

# %% ------ plpt evolution of cases -----
countries = ['Germany', 'Italy', 'France', 'United Kingdom', 'Brazil']

fig, ax = plt.subplots(1)
for i, country in enumerate(countries):
    days = confirmed.loc[country].index[-50:]
    cases = confirmed.loc[country].values[-50:]
    tode = deaths.loc[country].values[-50:]
    ax.plot(days, cases, label=countries[i])
    # ax.plot(days, np.log(cases), label=countries[i])
    # ax.xaxis.x
# ax.xaxis.set_major_locate(plt.MaxNLocator(5))
plt.legend()
plt.show()

# %% ------- display deaths and cofirmed cases

# extract data for wanted time span
start_date = '1/22/20'
end_date = deaths.columns[-1]
deaths_c = deaths.loc[countries, start_date:end_date]
conf_c = confirmed.loc[countries, start_date:end_date]

# set up figure and configure axis
fig2, axes = plt.subplots(2, 2)
fig2.set_figheight(12)
fig2.set_figwidth(10)
ax1 = axes[0, 0]
ax2 = axes[0, 1]
ax3 = axes[1, 0]
ax4 = axes[1, 1]
ax1.set_title('confirmed')
ax2.set_title('deaths')
ax3.set_title('confirmed')
ax4.set_title('deaths')

# plot data
for i, id in enumerate(deaths_c.index):
    data1 = conf_c.loc[id]
    data2 = deaths_c.loc[id]
    ax1.plot(data1.index, data1.values, label=id)
    ax2.plot(data2.index, data2.values, label=id)
    ax3.plot(data1.index, np.log(data1.values), label=id)
    ax4.plot(data2.index, np.log(data2.values), label=id)
    # plt.legend()
axes
for ax in axes.flatten():
    ax.xaxis.set_major_locator(plt.MaxNLocator(5))
    ax.legend()
plt.tight_layout()
plt.show()


# %% new cell
#ger = confirmed.loc['China']
#changes = ger.values[1:]-ger.values[:-1]
#plt.plot(ger.index[1:], changes)

deaths[confirmed.iloc[:, -1] > 20000].iloc[:, -3:]

# %%
rates = death_rate.loc[countries]
rates = rates.iloc[:, -50:]
for country in rates.index:
    plt.plot(rates.loc[country].values, label=country)
plt.legend()
plt.show()
