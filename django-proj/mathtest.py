# 1 + 1/1 + 1/1*2 + 1/1*2*3 = e
from decimal import Decimal

e = 1;
limit = 1000000

current = 1

for i in range(1, limit):
    current *= i
    e += Decimal(1/(current))

    if i % 5 == 0:
        print("e = {}" .format(e))
        print(i)
        print("=" * 10)

print(e)
