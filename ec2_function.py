#!/usr/bin/env python3

import pandas as pd
import math
import random

D=100
H=100
T='Buy'
P=5
    
data = pd.read_csv('NFLX_data.csv').set_index('Date')
#print(data.head())

minhistory = H
shots = D
time_horizon = P

dates = []
var95s = []
var99s = []
profits_losses = []

if T == 'Buy':

    for i in range(minhistory, len(data)):
        if data.Buy[i]==1:
            # if we’re interested in Buy signals
            mean=data.Close[i-minhistory:i].pct_change(1).mean()
            std=data.Close[i-minhistory:i].pct_change(1).std()
            # generate much larger random number series with same broad characteristics
            simulated = [random.gauss(mean,std) for x in range(shots)]
            # sort and pick 95% and 99%  - not distinguishing long/short risks here
            simulated.sort(reverse=True)
            var95 = simulated[int(len(simulated)*0.95)]
            var99 = simulated[int(len(simulated)*0.99)]

            price_at_buy = data.Close[i]
            price_at_sell = data.Close[i+time_horizon]
            profit_loss = price_at_sell - price_at_buy

            #print(data.index[i])
            #print(var95, var99) # so you can see what is being produced
            #print(profit_loss)
            dates.append(data.index[i])
            var95s.append(var95)
            var99s.append(var99)
            profits_losses.append(profit_loss)

elif T == 'Sell':

    for i in range(minhistory, len(data)):
        if data.Sell[i]==1:
            # if we’re interested in Buy signals
            mean=data.Close[i-minhistory:i].pct_change(1).mean()
            std=data.Close[i-minhistory:i].pct_change(1).std()
            # generate much larger random number series with same broad characteristics
            simulated = [random.gauss(mean,std) for x in range(shots)]
            # sort and pick 95% and 99%  - not distinguishing long/short risks here
            simulated.sort(reverse=True)
            var95 = simulated[int(len(simulated)*0.95)]
            var99 = simulated[int(len(simulated)*0.99)]

            price_at_buy = data.Close[i]
            price_at_sell = data.Close[i+time_horizon]
            profit_loss = price_at_buy - price_at_sell

            #print(data.index[i])
            #print(var95, var99) # so you can see what is being produced
            #print(profit_loss)
            dates.append(data.index[i])
            var95s.append(var95)
            var99s.append(var99)
            profits_losses.append(profit_loss)


table = pd.DataFrame({'Signal Date': dates, 'Risk 95%': var95s, 'Risk 99%': var99s, 'Profit/Loss': profits_losses})
#table.set_index('Signal Date', inplace=True)
print(table)
