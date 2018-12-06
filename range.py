import random
N = 2**64
c = 1000003

T = 100000
s = set()
for _ in range(T):
    s.add(random.randint(0,N-1))
print(random.randint(0,N-1))