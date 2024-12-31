digits = "23"
digiDict = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
biglen = 0
for i in range(len(digits)):
    biglen = max(len(digiDict[int(digits[i])]), biglen)
maxlen = biglen
adder = 1
words = ["" for i in range(len(digits)**maxlen+100)]
k = 0
for i in range(len(digits)):
    for j in digiDict[int(digits[i])]:
        while k < maxlen:
            print(k, j, maxlen)
            words[k + adder - 1] += j
            k += 1
        adder += 1
        maxlen += biglen
    k = 0
    maxlen = biglen
    
print(words) 