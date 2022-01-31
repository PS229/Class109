import csv
import statistics
import pandas as pd

df = pd.read_csv("height.csv")
heightlist = df["Height"].to_list()

mean = sum(heightlist)/len(heightlist)
median = statistics.median(heightlist)
mode = statistics.mode(heightlist)
std = statistics.stdev(heightlist)

firstst,firstend = mean - std, mean + std
secondst,secondend = mean - (2*std), mean + (2*std)
thirdst,thirdend = mean - (3*std), mean + (3*std)

firstlist = [result for result in heightlist if result>firstst and result<firstend]
secondlist = [result for result in heightlist if result>secondst and result<secondend]
thirdlist = [result for result in heightlist if result>thirdst and result<thirdend]

print("{}% of data lies within first std".format(len(firstlist)*100/len(heightlist)))
print("{}% of data lies within second std".format(len(secondlist)*100/len(heightlist)))
print("{}% of data lies within third std".format(len(thirdlist)*100/len(heightlist)))