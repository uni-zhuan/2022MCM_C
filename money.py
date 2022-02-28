#%%
from cProfile import label
from cmath import nan
from traceback import print_tb
from joblib import PrintTime
from matplotlib.axis import XTick
from mysqlx import Row
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white", context="talk")

date = pd.read_csv('lingmindu.csv')["date"]
price = pd.read_csv('lingmindu.csv')["moeny"]
iord=[]
# gain=[]

#%%
iord=[]
# gain=[]
iord.append(0)

# gain.append(1)

for i in range(1,len(date)-1):
    iord.append(price[i]-price[i-1])
    # gain.append((price[i]-1000)/1000)
    
iord.append(0)

# gain.append(1)
# print(gain)
# print(len(date),len(iord))
print(len(date),len(iord),len(price))

#%%

sns.set_theme(style="whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)

sns.barplot(x=date, y=price, palette="flare", ax=ax1)
ax1.axhline(0, color="k", clip_on=False)

# 
ax1.set_ylabel("Total money in $")

sns.barplot(x=date, y=iord, palette="crest", ax=ax2)
ax2.axhline(0, color="k", clip_on=False)    
ax2.set_ylabel("Increases or decreases in $")

# sns.barplot(x=date, y=gain, palette="viridis", ax=ax3)
# ax3.axhline(0, color="k", clip_on=False)
# ax3.set_ylabel("Percentage of yield(%)")

# x=[1,2,3,4,5]
# labels=['2016','2017','2018','2019','2020','2021']
sns.despine(bottom=True)
# f.set_xticks(ticks=['2016','2017','2018','2019','2020','2021'])
# plt.xticks(x,labels,rotation=60) 
# plt.setp(f.axes,yticks=[],xtick=[])
import matplotlib.ticker as ticker
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
plt.tight_layout(h_pad=2)

#%%
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

from cmath import nan
from traceback import print_tb
from joblib import PrintTime
from matplotlib.axis import XTick
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="ticks")

date = pd.read_csv('larger_rate_money.csv')["date"]
price = pd.read_csv('larger_rate_money.csv')["moeny"]

date2 = pd.read_csv('low_rate_money.csv')["date"]
price2 = pd.read_csv('low_rate_money.csv')["moeny"]

iord=[]
gain=[]

iord.append(0)

gain.append(1)

for i in range(1,len(date)-1):
    iord.append(price[i]-price[i-1])
    gain.append(price[i]-1000)

newlist1=DataFrame(columns=("Date","Price","index"))
newlist1['Date']=date
newlist1['Price']=price
newlist1['index']="Total money(low) in $"

newlist2=DataFrame(columns=("Price2","index2"))
# newlist2['Date']=date2
newlist2['Price2']=price2
newlist2['index2']="Total money(high) in $"

newlist=pd.concat([newlist1,newlist2],axis=1)

print(newlist)


print(len(newlist1),len(newlist2))

f, ax = plt.subplots(figsize=(17, 10))
# print(mydate)
sns.set_theme(style="whitegrid")
sns.set_color_codes("pastel")

s1=sns.barplot(
    x="Date", 
    y="Price",
    data=newlist,
    label="Total money(low) in $",
    color="b"
)

sns.set_color_codes("muted")

s2=sns.barplot(

    x="Date", 
    y="Price2",
    data=newlist,
    label="Total money(high) in $",
    color="r"
)


label=['Total money(low) in $','Total money(high) in $']
ax.legend(label,ncol=2,loc=1)
ax.set(xlim=(0,240), ylabel="Total money in $",
       xlabel="Date")
sns.despine(left=True, bottom=True)


# ax.xaxis.set_major_formatter(mpl.ticker.ScalarFormatter())
# ax.set_xticks(['2016','2017','2018','2019','2020','2021'])
# import matplotlib.ticker as ticker
# plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
# plt.tight_layout(h_pad=2)
#%%


from cProfile import label
from cmath import nan
from traceback import print_tb
from joblib import PrintTime
from matplotlib.axis import XTick
from mysqlx import Row
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="white", context="talk")

date = pd.read_csv('larger_rate_money.csv')["date"]
price = pd.read_csv('larger_rate_money.csv')["moeny"]

date2 = pd.read_csv('low_rate_money.csv')["date"]
price2 = pd.read_csv('low_rate_money.csv')["moeny"]




sns.set_theme(style="whitegrid")
f, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8), sharex=True)

sns.barplot(x=date, y=price, color='b', ax=ax1)
ax1.axhline(0, color="k", clip_on=False)
ax1.set_ylabel("Total money(low) in $")

sns.barplot(x=date, y=price2, color='r', ax=ax2)
ax2.axhline(0, color="k", clip_on=False)
ax2.set_ylabel("Total money(high) in $")

#ax3
# sns.set_color_codes("pastel")
# sns.barplot(
#     x="Date", 
#     y="Price",
#     data=newlist,
#     label="Total money(low) in $",
#     color="b"
# )


# sns.set_color_codes("muted")
# sns.barplot(
#     x="Date", 
#     y="Price2",
#     data=newlist,
#     label="Total money(high) in $",
#     color="r"
# )
# ax3.legend(label,ncol=2,loc=1)
# # ax.set(xlim=(0,240), ylabel="Total money(low) in $",
# #        xlabel="Date")
# ax3.axhline(0, color="k", clip_on=False)
# ax3.set_ylabel("Comparison of total money in $")



# x=[1,2,3,4,5]
# labels=['2016','2017','2018','2019','2020','2021']
sns.despine(bottom=True)
# f.set_xticks(ticks=['2016','2017','2018','2019','2020','2021'])
# plt.xticks(x,labels,rotation=60) 
# plt.setp(f.axes,yticks=[],xtick=[])
import matplotlib.ticker as ticker
plt.gca().xaxis.set_major_locator(ticker.MultipleLocator(40))
plt.tight_layout(h_pad=2)