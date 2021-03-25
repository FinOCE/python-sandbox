import math

pi = 0
for i in range(1, 100000000):
    pi += 1/(i*i)
pi = math.sqrt(pi*6)
print(math.pi)
print(pi)