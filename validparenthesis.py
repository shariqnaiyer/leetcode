s = "(){}}{"
from collections import deque
p  = deque(s)
q  = deque() 
q.append(p.popleft())

d  = {"(":")", "{":"}", "[":"]"}
while p:
    print("p: ", p)
    print("q: ", q)
    a = p[0]
    b = q[-1]
    if b in d:
        if d[b] == a:
            p.popleft()
            q.pop()
            if not q and p:
                q.append(p.popleft()) 
        else:
            q.append(a)
            p.popleft()
    else:
        break

print("p: ", p)
print("q: ", q)
if p:
    print(False)
else:
    print(True)