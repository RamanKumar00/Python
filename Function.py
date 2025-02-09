def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("A is greater")
    else:
        print('B is Greater or Equal')
        
a = 5
b = 8
isGreater(a,b)

calculateGmean(a,b)