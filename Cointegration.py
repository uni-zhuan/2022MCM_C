# %%
from cmath import nan
from traceback import print_tb
from joblib import PrintTime
import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

a_price = pd.read_csv('LBMA-GOLD.csv')["USD (PM)"]
a_date = pd.read_csv('LBMA-GOLD.csv')["Date"]

b_price = pd.read_csv('BCHAIN-MKPRU.csv')["Value"]
b_date = pd.read_csv('BCHAIN-MKPRU.csv')["Date"]
print(a_date)
print(b_date)

# %%

a_newprice = []
a_new_date = []

b_newprice = []
b_new_date = []

b_add = 0
a_add = 0
for i in range(0, len(a_date)):
    if(a_date[i+a_add] == b_date[i+b_add]):

        # a_newprice.append(a_price[i+a_add])
        # a_new_date.append(a_date[i+a_add])
        # print(b_add,a_date[i],b_date[i+b_add])
        b_newprice.append(b_price[i+b_add])
        b_new_date.append(b_date[i+b_add])
    elif(a_date[i+a_add]>b_date[i+b_add]):
        b_add=b_add+1
        b_newprice.append(b_price[i+b_add])
        b_new_date.append(b_date[i+b_add])
        # print(b_add,a_date[i],b_date[i+b_add])
    # elif(a_date[i+a_add]<b_date[i+b_add]):
    #     a_add=a_add+1
print(len(b_newprice))
print(len(a_price))

print(b_newprice)


print(a_price)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(range(350,1000), a_price[350:1000]*10)
ax.plot(range(350,1000), b_newprice[350:1000])
ax.legend(['gold','bitc'])
plt.show()
#%%
from pandas.core.frame import DataFrame
asset=[a_price[350:1000]*10,b_newprice[350:1000]]

date=a_date[350:1000]
goldprice=a_price[350:1000]*10
bitprice=b_newprice[350:1000]

# date=a_date[0:1190]

# goldprice=a_price[0:1190]*10
# bitprice=b_newprice[0:1190]

# new_data={"Date":a_date[350:1000],"a_price":a_price[350:1000]*10,"b_newprice":b_newprice[350:1000]}
newlist1=DataFrame(columns=("Date","Price","Asset"))
newlist1['Date']=date
newlist1['Price']=goldprice
newlist1['Asset']="Gold"

newlist2=DataFrame(columns=("Date","Price","Asset"))
newlist2['Date']=date
newlist2['Price']=bitprice
newlist2['Asset']="Bitcoin"

newlist=pd.concat([newlist1,newlist2],axis=0,ignore_index=True)

import seaborn as sns
from matplotlib import rcParams

# plt.figure(figsize=(20,8))
# rcParams['figure.figsize'] = 15,8
sns.set_theme(style="darkgrid")
sns.set_style("darkgrid", {"axes.facecolor": ".9"})
sns.set(rc={'figure.figsize':(10, 6)})
# cm = sns.color_palette('coolwarm', as_cmap=True)
p=sns.relplot(x="Date",y="Price",hue="Asset", kind="line", data=newlist,height=8, aspect=15/8,palette=["b", "r"]);
p.set(xticks=np.arange(0,1300,80))


#%%
import seaborn as sns
sns.set_theme(style="whitegrid")

# Load the brain networks dataset, select subset, and collapse the multi-index
df = sns.load_dataset("brain_networks", header=[0, 1, 2], index_col=0)

used_networks = [1, 5, 6, 7, 8, 12, 13, 17]
used_columns = (df.columns
                  .get_level_values("network")
                  .astype(int)
                  .isin(used_networks))
df = df.loc[:, used_columns]

df.columns = df.columns.map("-".join)

# Compute a correlation matrix and convert to long-form
corr_mat = df.corr().stack().reset_index(name="correlation")

# Draw each cell as a scatter point with varying size and color
g = sns.relplot(
    data=corr_mat,
    x="level_0", y="level_1", hue="correlation", size="correlation",
    palette="vlag", hue_norm=(-1, 1), edgecolor=".7",
    height=10, sizes=(50, 250), size_norm=(-.2, .8),
)

# Tweak the figure to finalize
g.set(xlabel="", ylabel="", aspect="equal")
g.despine(left=True, bottom=True)
g.ax.margins(.02)
for label in g.ax.get_xticklabels():
    label.set_rotation(90)
for artist in g.legend.legendHandles:
    artist.set_edgecolor(".7")

#%%
# Hexbin plot with marginal distributions 绿色的
import numpy as np
import seaborn as sns
sns.set_theme(style="white")

goldprice=a_price[350:1000]*10

bitprice=b_newprice[350:1000]

sns.jointplot(x=goldprice, y=bitprice, kind="hex", color="#4CB391")

#%%
#黑洞 0-1190
import seaborn as sns
sns.set_theme(style="ticks")

goldprice=a_price[500:800]*10

bitprice=b_newprice[500:800]

g = sns.JointGrid(x=goldprice, y=bitprice, space=0)
g.plot_joint(sns.kdeplot,
             fill=True, 
             thresh=0, levels=100, cmap="rocket")
g.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=25)
# %%
# ADF检验：两个序列是否是一阶单整的
from statsmodels.tsa.stattools import adfuller


gold_price = np.reshape(a_price*10, -1)
# console: MissingDataError: exog contains inf or nans adfuller
# print(gold_price.isna().sum())
gold_price = gold_price.dropna()
# gold_price.isnull().sum()
# gold_price.dropna(axis=0)

gold_price_diff = np.diff(gold_price[350:1000])

bitc_price = np.reshape(b_price, -1)

bitc_price_diff = np.diff(bitc_price[350:1000])

# print(None in gold_price_diff )
print(adfuller(gold_price_diff))


print(adfuller(bitc_price_diff))
 
# result:
# https://blog.csdn.net/FrankieHello/article/details/86766625
# (-12.443649569313777, 3.705609676662802e-23, 6, 988, {'1%': -3.4369860032923145, '5%': -2.8644697838498376, '10%': -2.5683299626694422}, 12167.346579799874)
# (-5.453484744988983, 2.612767642385308e-06, 20, 978, {'1%': -3.437054035425408, '5%': -2.8644997864059363, '10%': -2.5683459429326576}, 14027.877806400826)


# adfuller函数的参数意义分别是：
# x：一维的数据序列。
# maxlag：最大滞后数目。
# regression：回归中的包含项（c：只有常数项，默认；ct：常数项和趋势项；ctt：常数项，线性二次项；nc：没有常数项和趋势项）
# autolag：自动选择滞后数目（AIC：赤池信息准则，默认；BIC：贝叶斯信息准则；t-stat：基于maxlag，从maxlag开始并删除一个滞后直到最后一个滞后长度基于 t-statistic 显著性小于5%为止；None：使用maxlag指定的滞后）
# store：True  False，默认。
# regresults：True 完整的回归结果将返回。False，默认。
# 返回值意义为：
# adf：Test statistic，T检验，假设检验值。
# pvalue：假设检验结果。
# usedlag：使用的滞后阶数。
# nobs：用于ADF回归和计算临界值用到的观测值数目。
# icbest：如果autolag不是None的话，返回最大的信息准则值。
# resstore：将结果合并为一个dummy。
 
#%%
#  判断两者是否存在协整关系
from statsmodels.tsa.stattools import coint
 
print(coint(gold_price[350:1000], bitc_price[350:1000]))

# result:
# (-0.4526329302232922, 0.9675378530500833, array([-3.91339464, -3.34556084, -3.05099143]))
# 从返回结果可以看出 t-statistic 值要小于1%的置信度，所以有99%的把握拒绝原假设，而且p-value的值也比较小，所以说存在协整关系。


#%%
import seaborn as sns
sns.set_theme(style="ticks")

dots = sns.load_dataset("dots")

# Define the palette as a list to specify exact values
palette = sns.color_palette("rocket_r")

# Plot the lines on two facets
sns.relplot(
    data=dots,
    x="time", y="firing_rate",
    hue="coherence", size="choice", col="align",
    kind="line", size_order=["T1", "T2"], palette=palette,
    height=5, aspect=.75, facet_kws=dict(sharex=False),
)