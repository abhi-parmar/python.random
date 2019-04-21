def cf():
    import pickle
    f=open('indexfile','wb')
    index=dict()
    start=0
    for x in range(10000):
        temp=[]
        for z in range(10):
            temp.append(start)
            start+=1
        index[x]=temp
    pickle.dump(index,f)
    f.close()
    pkl=open('indexfile','rb')
    dic=pickle.load(pkl)
    dic=dict(dic)
    te=open('ww','w+')
    for z,y in dic.items():
        w=str(z)+':'+str(y)
        te.write(w)
        te.write('\n')
    pkl.close()
    te.close()
    te=open('ww','r')
    print(te.read())
    x=int(input('\nenter a number to search between 0 - 99999 \n'))
    if x>100000:
        print('\ninvalid')
        return
    t=str(x)[-1]
    ind=x-int(t)
    ind=str(ind)
    ind=ind[0:len(ind)-1]
    ind=int(ind)
    pkl=open('indexfile','rb')
    dic=pickle.load(pkl)
    keycount=0
    valcount=0
    for i in dic.keys():
        keycount+=1
        if ind==i:
            print('index found after iterations :',keycount)
            for j in dic[i]:
                valcount+=1
                if x==j:
                    print('value found after iterations',valcount)
                    print('total iterations:',keycount+valcount)
                    break
            
    
    
cf()
