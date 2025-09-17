import sys 
if len(sys.argv)!= 2:print("none");exit()
print("Good job~~!!" if (input("What was the parameter? ")==sys.argv[1]) else "Nope, sorry~~")

#python3 parameter_matching.py "Fute"