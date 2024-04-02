from collections import deque

aux = deque()

n = int(input())
stack = list(map(int, input().split()))
stack = deque(stack)


num = 0
while len(stack)!= 0:
    a = stack[-1]
    b = stack[-1]
    aux.append(b)
    print(num, a, b, stack, aux)
    if a == b:
        print(stack.pop())
        print(aux.pop())
    else:
        aux.append(stack.pop())