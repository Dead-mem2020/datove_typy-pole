import random

low = 0
high = 100
cols = 5
rows = 3

x = [random.choices(range(low,high), k=cols) for i in range(rows)]

print(x)