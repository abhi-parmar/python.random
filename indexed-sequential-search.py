def cf():
    import pickle
    f=open('indexfile','wb')
    index=dict()                   #creates empty dictionary , which will be dumped to indexfile.
    start=0
    for x in range(10000):         
        temp=[]                    #creating new array after every iteration 
        for z in range(10):         #appending values to temp array , starting from (start) value everytime.
            temp.append(start)      # 10 numbers per list (index funciton). 1 key in dictionary for 1 list of 10 elements as value 
            start+=1                #open ww file for example.
        index[x]=temp
    pickle.dump(index,f)             #pickle dump to indexfile.         
    f.close()
    pkl=open('indexfile','rb')
    dic=pickle.load(pkl)
    dic=dict(dic)
    te=open('ww','w+')               #just to visualise the index file created above.
    for z,y in dic.items():
        w=str(z)+':'+str(y)
        te.write(w)
        te.write('\n')
    pkl.close()
    te.close()
    te=open('ww','r')
    print(te.read())                 #visualisation ends here
    x=int(input('\nenter a number to search between 0 - 99999 \n'))   #user input for search value.
    if x>100000:
        print('\ninvalid')
        return
    t=str(x)[-1]                       #calculate the index value from user input.
    ind=x-int(t)
    ind=str(ind)
    ind=ind[0:len(ind)-1]
    ind=int(ind)
    pkl=open('indexfile','rb')
    dic=pickle.load(pkl)
    keycount=0
    valcount=0
    for i in dic.keys():              #search index in indexfile.
        keycount+=1
        if ind==i:
            print('index found after iterations :',keycount)
            for j in dic[i]:                                    #search user input value in values at index found.
                valcount+=1
                if x==j:
                    print('value found after iterations',valcount)
                    print('total iterations:',keycount+valcount)
                    break
            
    
    
cf()
