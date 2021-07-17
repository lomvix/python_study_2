from die import Die
from plotly import offline
from plotly.graph_objs import Bar ,Layout

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll()+die2.roll()
    results.append(result)

frequencies =[]
max_result = die1.num_sides+die2.num_sides
for value in range(2,max_result+1):
    frequency =results.count(value)
    frequencies.append(frequency)

x_values =list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title = '掷两个D6 1000 次的结果', xaxis = x_axis_config , yaxis = y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename = 'visual.html')

