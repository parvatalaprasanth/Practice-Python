# Python program to solve
# Gold Mine problem

MAX = 100

# Returns maximum amount of
# gold that can be collected
# when journey started from
# first column and moves
# allowed are right, right-up
# and right-down
def getMaxGold(gold, m, n):
    dp={}
    def get(gold,i,j):
        if i<0 or i>=m:
            return 0
        if j<0 or j>=n:
            return 0
        if (i,j) in dp:
            return dp[(i,j)]
        dp[(i,j)]=gold[i][j]+max(get(gold,i,j+1),get(gold,i-1,j+1),get(gold,i+1,j+1))
        return dp[(i,j)]
    ans=0
    for i in range(n):
        ans=max(ans,get(gold,i,0))
    return ans
	
# Driver code
gold = [[1, 3, 1, 5],
	[2, 2, 4, 1],
	[5, 0, 2, 3],
	[0, 6, 1, 2]]

m = 4
n = 4

print(getMaxGold(gold, m, n))

# This code is contributed
# by Soumen Ghosh.			
