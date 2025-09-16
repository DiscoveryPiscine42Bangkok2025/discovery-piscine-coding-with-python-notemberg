x,y = 0,0
while x <=10: 
    print(f"Table of {x}: ",end="")
    y=0
    while y<=10:
        print(f"{x*y} ",end="")
        y +=1
    print("")
    x+=1

    
    
#for x in range(11):
#    print(f"Table of {x}: ", " ".join(str(x * y) for y in range(11)))