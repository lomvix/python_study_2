import csv
import matplotlib.pyplot as plt
from datetime import datetime
from pylab import *  

filename = 'data/sitka_weather_2018_simple.csv'
mpl.rcParams['font.sans-serif'] = ['SimHei']  
matplotlib.rcParams['axes.unicode_minus'] =False
f = open(filename,'r')
reader = csv.reader(f)
header_row = next(reader)

dates,highs,lows = [],[],[]
for row in reader :
    current_date = datetime.datetime.strptime(row[2], '%Y-%m-%d')
    high = int (row[5])
    low = int(row[6])
    lows.append(low)
    dates.append( current_date)
    highs.append(high)

fig, ax = plt.subplots()
ax.plot(dates,highs,c='red', alpha = 0.5)
ax.plot(dates,lows,c = 'blue', alpha = 0.5)
ax.fill_between(dates,highs,lows,facecolor = 'blue', alpha =0.1)

ax.set_title("2018年每日最高温度",fontsize =24)
ax.set_xlabel('',fontsize = 16)
fig.autofmt_xdate()
ax.set_ylabel("温度（F）",fontsize = 16)
ax.tick_params(axis = 'both',which = 'major',labelsize = 16)

plt.show()