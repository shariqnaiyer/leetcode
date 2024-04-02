dp = {}
def climbStairs(n):
	"""
	:type n: int
	:rtype: int
	"""
	print("cat", climbStairs(n-2))
	if n in dp:
		return dp[n]
		
	if n == 0:
		return 1

	if n < 0:
		dp[n] = 0
		return 0


	dp[n] = climbStairs(n-1) + climbStairs(n-2)
	return dp[n]

climbStairs(1)
print(climbStairs(1))