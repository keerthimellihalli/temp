import sys

if len(sys.argv) == 2:
    temp = float(sys.argv[1])
else:
    temp = 25  # default value

if temp < 15:
    print("Cold")
elif temp <= 30:
    print("Normal")
else:
    print("Hot")
