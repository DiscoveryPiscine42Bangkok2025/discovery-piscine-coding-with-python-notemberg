import sys
print(*reversed(sys.argv[1:])) if len(sys.argv) > 3 else print("none") 

#python3 aff_rev_params.py xxxx yyyy zzzz
#expected zzzz yyyy xxxx