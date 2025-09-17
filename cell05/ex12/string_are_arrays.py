import sys
print("".join(c for c in sys.argv[1:][0] if c == 'z') or "none" if len(sys.argv[1:])==1 else "none")

#python3 string_are_arrays.py "Zfsazzdf ASdz dazsd zzz"
#expected zzzzzzz