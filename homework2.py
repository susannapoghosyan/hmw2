from __future__ import division
mylist=input("Please input numbers seperated by comma")
def mean(mylist):
    return sum(mylist)/len(mylist)
print mean(mylist)
from __future__ import division
list=input("please input some numbers seperated by comma")
n_of_o=input("please input number of occurancies")
def avg(list):
    return sum(list[len(list)-n_of_o:])/n_of_o
print avg(list)
import random
a=random.randint(1,100)
print a
def function(a):
        if a<100 and a>50:
            return "Win"
        elif a<=50 and a>=1:
            return "Loss"
        elif a==100:
            return "Draw"
print function(a)
import pandas_datareader.data as web
list2=[web.DataReader("SBUX","google"),web.DataReader("NFLX","google"),web.DataReader("NKE","google")]
for stock in list2:
    print stock.head(7)
    import matplotlib.pyplot as plt
    for stock in list2:
    plt.plot(stock)
    plt.show()