import sys 
print("\n".join([f"{arg}:{len(arg)}" for arg in sys.argv[1:]])) if len(sys.argv) > 2 else print("none")

#python3 count_it.py asd fghgffgh gkghj
#expected
#asd:3
#fghgffgh:8
#gkghj:5