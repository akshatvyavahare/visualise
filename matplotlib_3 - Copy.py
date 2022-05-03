# visualisation the weather data for specific year

from cProfile import label
import matplotlib.pyplot as plt     
import numpy as np
import pandas as pd

weather = pd.read_csv(r'C:\Users\aksha\Desktop\weather_madrid_LEMD_1997_2015.csv', header = 0, index_col=None)

print(weather)

weather['Date']= pd.to_datetime(weather['Date'])

weather['Day']= weather['Date'].dt.day
weather['Month']= weather['Date'].dt.month
weather['Year']= weather['Date'].dt.year

print(weather)

print(weather.dtypes)


df_year = weather[
      (weather['Year'] >= 2013)
]

plt.title('Weather Data')
plt.Line2D(df_year.Year, df_year['Max TemperatureC'], label='Max')
plt.Line2D(df_year.Year, df_year['Mean TemperatureC'], label='Mean')
plt.Line2D(df_year.Year, df_year['Min TemperatureC'], label='mmm')

plt.xlabel('date')
plt.ylabel('temp')

plt.legend()
plt.show()