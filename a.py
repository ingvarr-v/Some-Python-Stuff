maxX9=1
minX9=1001
for x in range(1,1000):
    positive = -1
    x10=x
    Xtest=x10
    x9 = ''
    while(x10>0):
        x9=str(x10%9)+x9
        x10=x10//9
    X9=int(x9)
    
    if(X9//1000==0 and X9//100!=0):
        X9test=X9
        while(X9test>0):
            if(X9test%10==3):
                positive=1
            X9test=X9test//10
        if(positive==1):
            FinalX9=''
            MultipliedX = Xtest*3
            while(MultipliedX>0):
                FinalX9=str(MultipliedX%9)+FinalX9
                MultipliedX=MultipliedX//9
            FinalX9=int(FinalX9)
        
            if(FinalX9//1000==0 and FinalX9//100!=0):

##                print(X9)
                if(X9<minX9):
                    minX9=X9
                if(X9>maxX9):
                    maxX9=X9

##print(minX9)
##print(maxX9)

Sum=minX9+maxX9

print(Sum)
