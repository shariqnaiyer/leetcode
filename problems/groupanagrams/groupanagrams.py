# k = int(input())
# p = []
# for i in range(k):
#     p.append(int(input()))

# p.sort()
# max = k
# a = 0
# b = k - 1
# while a < k:
#     if p[a] < max:
#         max -= 1
#     a += 1
# print(max)



# def fun(k,p):
#     p.sort()
#     max = k
#     # for i in range(k):
#         # print(p[i])
#     a = 0
#     b = k - 1
#     while a < b:
#         if p[a] < k:
#             k -= 1
#         a+=1
#     print(k)


# import random
# p = []
# k = random.randint(5,15)
# for i in range(k):
#     p.append(random.randint(0,10))

# print(k,p)
# fun(k,p)

# while True:
#     line = input()
#     if line == '':
#         break
#     lena, num = map(int, line.split())
#     right = []
#     left = []
#     for i in range(num):
#         mag, dirt = map(str, input().split())
#         if dirt == "L":
#             left.append(int(mag))
#         else: 
#             right.append(int(mag))

#     right.sort()
#     left.sort()

# for i in range(int(input())):
#     a, b = map(int(input().split()))
#     for i in range(a):
#         p = input()

# books, shops = map(int,input().split())
# dic = []
# l = []
# for i in range(shops):
#     k, postage = map(int,input().split()) 
#     for i in range(k):
#         a, b = map(int,input().split()) 
#         if a not in dic:
#             dic[a] = b+postage
#         if a in dic:
#             if dic[a] > b+postage:
#                 dic[a] = b+postage

#     print(dic)

# p = sum(dic.values())
# print(p)
# print(dic)

# import math
# for i in range(int(input())):
#     a,b,c = map(int, input().split())
#     moves = 0 
#     if a != b:
#         moves = math.ceil(abs(a-b)/(2*c))
#     print(moves)
    

teque = []
for i in range(int(input())):
    a, b = map(str, input().split())
    if a == "push_front":
        teque = [int(b)] + teque
    if a == "push_back":
        teque = teque + [int(b)]
    if a == "push_middle":
        k = len(teque)
        if k%2 == 0:
            teque = teque[:k//2] + [int(b)] + teque[k//2:]
        else:
            teque = teque[:(k+1)//2] + [int(b)] + teque[(k+1)//2:]
    if a == "get":
        print(teque[int(b)])