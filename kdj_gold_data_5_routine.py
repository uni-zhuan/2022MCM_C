#%%
import pandas as pd
import csv

data=pd.read_csv("LBMA-GOLD.csv")
print(len(data))
print(data[0:3])

# %%
usd=data["USD (PM)"]
value=data["Volume"]
date=data["Date"]

f=open("gold_kdj.csv",'w')
writer=csv.writer(f)
header=['date','open','high','low','close','value']
writer.writerow(header)

for i in range(0,int(1246/3)):
    save=[]
    sum_vol=0
    for j in range(0,3):
        save.append(usd[i*3+j])
        sum_vol+=value[i*3+j]
    # print(save[0])
    opendata=save[0]
    closedata=save[2]
    # print(type(save))
    highdata=max(list(save))
    lowdata=min(list(save))
    # print('['+date[3*i]+'-'+date[3*i+2],',',opendata,',',highdata,',',lowdata,',',closedata,',',sum_vol+']')
    newline=[date[3*i]+'-'+date[3*i+2],opendata,highdata,lowdata,closedata,sum_vol]
    # newline=[list(str('['+date[3*i]+'-'+date[3*i+2]+','+opendata+','+highdata+','+lowdata+','+closedata+','+sum_vol+']'))]

    # newline=['[\''+str(date[3*i])+'\','+str(opendata/10)+','+str(highdata/10)+','+str(lowdata/10)+','+str(closedata/10)+','+str(sum_vol)+'],']
    writer.writerow(newline)  
f.close() 


# %%
