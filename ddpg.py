def Step1(num , i):
    K1=0.05
    K2=0.05
    if (num == 1):
        HH=0
        LC=0
        HC=0
        LL=0
        if (i>=1):
            for j in range(1,2):
                HH = max(HH,data1['high'][j])
                HC = max(HC,data1['close'][j])
                LC = min(LC,data1['close'][j])
                LL = min(LL,data1['low'][j])
            rang=max((HH-LC),(HC-LL))
            Buyline = data1['open'][i]+K1*rang
            Sellline = data1['open'][i]-K2*rang
        else:
            Buyline = data1['high'][i-1]
            Sellline = data1['low'][i-1]*0.99
        min_ = 0
        if (i>=14):
            for j in range(2,15):
                min_ = min(min_,data1['low'][i-j])
        else: min_ = data1['low'][0]
        min_1 = 0
        if (i>=30):
            for j in range(0,14):
                min_1 = min(min_1,data1['low'][i-j])
            
        average = (data1['low'][i]+data1['high'][i]+data1['open'][i]+data1['close'][i])/4
       
        if ((wallet['gold'] == 0 )&( wallet['bitc'] == 0)):
            if (
                (min_1>min_)|
                (data1['close'][i] >= min_)|
                (data1['close'][i] >= Buyline) | 
                (data1['close'][i] <average*0.98)
               ):
                    
                money = wallet['USD']
                wallet['USD']=0
                wallet['bitc']=money*(1-0.02)/data1['open'][i]
            elif ((data1['open'][i] <= Sellline)):
                money = wallet['USD']
                wallet['USD']=0
                wallet['bitc']=money*(1-0.02)/data1['open'][i]
            return
            
        if (data1['close'][i-1]>data1['open'][i-1]):  
            if (data1['close'][i] < Sellline):
                money = wallet['bitc']
                wallet['bitc']=0
                wallet['USD']=money * data1['open'][i] * 0.98
                return
        elif (data1['close'][i-1]<data1['open'][i-1]):
            if (data1['close'][i] > Buyline):
                money = wallet['bitc']
                wallet['bitc']=0
                wallet['USD']=money * data1['open'][i] * 0.98
                return
wallet = {'USD':1000 ,'gold': 0 , 'bitc': 0}
final = []

final.append(wallet['USD'])
print(wallet,'USD:' ,wallet['USD'])
for i in range(1,min(len(data1),len(data2))):
    if ((data1['close'][i]-data1['open'][i]<0)&(data2['close'][i]-data2['open'][i]<0)&(wallet['USD']!=0)):
        final.append(wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        print(wallet,'USD:' ,wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        continue
    if (wallet['bitc']!=0 & (wallet['USD']==0 & (data1['open'][i]>data1['open'][i-1]))):
        money = wallet['bitc']
        wallet['bitc']=0
        wallet['USD']=money * data1['open'][i] * 0.98
        final.append(wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        print(wallet,'USD:' ,wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        continue
    elif(wallet['gold']!=0 & (wallet['USD']==0 & (data2['open'][i]>data2['open'][i-1]))):
        money = wallet['gold']
        wallet['gold']=0
        wallet['USD']=money * data2['open'][i] * 0.99
        final.append(wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        print(wallet,'USD:' ,wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
        continue
    if ((data1['close'][i]-data1['open'][i])/data1['close'][i] >= (data2['close'][i]-data2['open'][i])/data2['close'][i]):
        Step1(1,i) 
    else :
        Step1(2,i) 
    final.append(wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
    print(wallet,'USD:' ,wallet['USD']+wallet['gold']*data2['open'][i]*1+wallet['bitc']*data1['open'][i]*0.98)
   