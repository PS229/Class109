import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
diceresult = []
for x in range(0,10000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceresult.append(dice1 + dice2)
#sum = 0
#for x in diceresult:
    #sum = sum + x
mean = sum(diceresult)/len(diceresult)
std = statistics.stdev(diceresult)
median = statistics.median(diceresult)
mode = statistics.mode(diceresult)

firststdevst,firststdevend = mean - std, mean + std
secondstdevst,secondstdevend = mean-(2*std), mean+(2*std)
thirdstdevst,thirdstdevend = mean-(3*std), mean+(3*std)

firstdata = [result for result in diceresult if result > firststdevst and result < firststdevend]
seconddata = [result for result in diceresult if result > secondstdevst and result < secondstdevend]
thirddata = [result for result in diceresult if result > thirdstdevst and result < thirdstdevend]

print("{}% of data lies within first std".format(len(firstdata)*100/len(diceresult)))
print("{}% of data lies within second std".format(len(seconddata)*100/len(diceresult)))
print("{}% of data lies within third std".format(len(thirddata)*100/len(diceresult)))

print(mean)
print(std)
print(median)
print(mode)

fig = ff.create_distplot([diceresult],["result"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = "lines", name = "mean"))
fig.add_trace(go.Scatter(x = [firststdevst,firststdevst], y = [0,0.17], mode = "lines", name = "stdev1"))
fig.add_trace(go.Scatter(x = [firststdevend,firststdevend], y = [0,0.17], mode = "lines", name = "stdev1"))
fig.add_trace(go.Scatter(x = [secondstdevst,secondstdevst], y = [0,0.17], mode = "lines", name = "stdev2"))                     
fig.add_trace(go.Scatter(x = [secondstdevend,secondstdevend], y = [0,0.17], mode = "lines", name = "stdev2"))
fig.show()