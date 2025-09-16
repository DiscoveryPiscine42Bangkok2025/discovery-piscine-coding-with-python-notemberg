x=[2,8,9,48,8,22,-12,2]
print(f"1st Arr {x}\n2nd Arr {set([int(i)+2 for i in x if i > 5])}")