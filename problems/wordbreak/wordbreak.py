# s = "leetcode"
# wordDict = ["leet","code"]

# s = "applepenapple"
# wordDict = ["apple","pen"]

# s = "aaaaaaa"
# wordDict = ["aaaa","aaa"]   

s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]

bigDict = {x:1 for x in wordDict}
for aword in wordDict:
    for another in wordDict:
        if aword != another and aword in another:
            bigDict[another] += bigDict[aword]

print(bigDict)


dp = [0 for i in range(len(s))]
word = ""
for i in range(len(s)):
    word += s[i]
    if word in wordDict:
        dp[i] += dp[i - 1] + bigDict[word]
    else:
        dp[i] = dp[i - 1]

print(dp)
print(dp[-1] > dp[-2])
