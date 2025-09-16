import sys 
print(f"{sys.argv[1].lower()}") if len(sys.argv) == 2 else print("none") 

#python3 downcase_it.py YFASF
#expected yfasf