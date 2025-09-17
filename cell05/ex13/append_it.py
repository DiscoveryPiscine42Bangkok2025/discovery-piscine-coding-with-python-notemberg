import sys
print("\n".join(f"{x}ism" for x in sys.argv[1:] if not x.endswith("ism")) if len(sys.argv) > 1 else "none")

#python3 append_it.py "xxxx" "yyyism" "zzzzzz"
#expected
#xxxxism
#zzzzzzism

