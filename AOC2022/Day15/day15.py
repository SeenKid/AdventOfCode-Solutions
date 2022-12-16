t=[x for x in open("input.txt")]; Y = 2000000; K = 4000000

s={}; b=set() # sensors, beacons
for l in t:
  sx,sy,bx,by = map(int,''.join(c for c in l if c in '=-0123456789')[1:].split("="))
  s[(sx,sy)] = abs(sx-bx)+abs(sy-by)
  b.add(by) # don't need bx

def intersected(a1,a2,b1,b2): # it's for union, so -1+1 to include adjacent
  return a1-1<=b1<=a2+1 or a1-1<=b2<=a2+1 or b1-1<=a1<=b2+1 or b1-1<=a2<=b2+1

def union(u,a1,a2):
  o = [] # old
  n = [] # united
  for u1,u2 in u:
    if intersected(u1,u2,a1,a2): n.append((min(u1,a1),max(u2,a2)))
    else: o.append((u1,u2))
  if not n: return o+[(a1,a2)]
  for n1,n2 in n: o = union(o,n1,n2)
  return o

def inter_lozenge_hline(sx,sy,r,y):
  if abs(sy-y)>r: return ()
  return (sx-(r-abs(sy-y)),sx+(r-abs(sy-y)))

u = []
for (sx,sy),r in s.items():
  x1x2 = inter_lozenge_hline(sx,sy,r,Y)
  if x1x2: u = union(u,*x1x2)

p1 = u[0][1]-u[0][0]+1-sum(by==Y for by in b)

def xy2pq(x,y): return (x-y,x+y)
def pq2xy(p,q): return ((p+q)//2,(q-p)//2)

pq = []
for (sx,sy),r in s.items():
  pq += [xy2pq(sx,sy+r),xy2pq(sx-r,sy),xy2pq(sx+r,sy),xy2pq(sx,sy-r)]

pp = sorted(set(p for p,_ in pq))
qq = sorted(set(q for _,q in pq))

p = [a+1 for a,b in zip(pp,pp[1:]) if b-a==2][0]
q = [a+1 for a,b in zip(qq,qq[1:]) if b-a==2][0]
x,y = pq2xy(p,q)

print(p1,x*K+y)