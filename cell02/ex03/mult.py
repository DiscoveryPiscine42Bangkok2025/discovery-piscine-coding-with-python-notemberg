x,y =int(input("1st num :\n")),int(input("2st num :\n"))
p =x*y
print(f"{x} x {y} = {p}\n{p} is",["both neg and pos","positive","negative"][(p>0)-(p<0)])