import sys 
print(f"{sys.argv[1].upper()}") if len(sys.argv) == 2 else print("none") 

#python3 upcase_it.py xyyy
#expected XYYY