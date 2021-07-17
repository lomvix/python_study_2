import matplotlib.pyplot as plt
'''
from pylab import *  
mpl.rcParams['font.sans-serif'] = ['SimHei']  
matplotlib.rcParams['axes.unicode_minus'] =False

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]

#plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(input_values,squares, linewidth=3)

ax.set_title("平方数", fontsize = 24)
ax.set_xlabel("值", fontsize = 4)
ax.set_ylabel("值的平方", fontsize =14)

ax.tick_params(axis = 'both', labelsize = 14)

plt.show()
'''
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

fig , ax = plt. subplots()
ax.scatter(x_values,y_values, s=10, cmap = plt.cm .Blues,c = y_values)
ax.axis([0,1100,0,1100000])

plt.savefig('squares_plot.png',bbox_inches = 'tight')
plt.show()