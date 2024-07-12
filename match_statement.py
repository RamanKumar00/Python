x=int(input("enter the value of x: "))

match x:
    
    case 1:
        print("value of x is 1")
        
    case 2:
        print("value of x is 2")
        
    case 3:
        print("value of x is 3")
        
    case _ :
        print("case not matched")