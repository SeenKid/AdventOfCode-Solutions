import time,sys
from collections import deque 
start=time.time()

inf = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
with open(inf) as fi:
    M= [int(x) for x in  fi.readlines()]
i=0
dM = []
key = 811589153
dD = deque([])
D= deque([])
for x in M:
    dx = key * x
    D.append((x,i))
    dD.append((dx,i))
    dM.append(dx)
    if x == 0:
        N = (0,i)
    i+=1

def find(D,x,dist):
    D.rotate(-D.index(x))
    D.rotate(-dist)
    val,pos = D.popleft()
    D.appendleft((val,pos))
    return val,pos

def move(D,x,i):
    D.rotate(-D.index((x,i)))
    D.popleft()
    D.rotate(-x)
    D.appendleft((x,i))
    return D

for i,x in enumerate(M):
    D = move(D,x,i)
print('part1:', find(D,N,1000)[0]+find(D,N,2000)[0]+find(D,N,3000)[0])

for _ in range(10):
    for i,x in enumerate(dM):
        dD = move(dD,x,i)
print('part2:', find(dD,N,1000)[0]+find(dD,N,2000)[0]+find(dD,N,3000)[0])

end=time.time()
print(round(end-start,5))