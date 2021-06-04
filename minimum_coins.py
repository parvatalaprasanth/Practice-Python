import sys
dp={}
def minCoins(coins, m, V):
    if V==0:
        return 0
    if V<0:
        return 999999
    res=999999
    if V in dp:
        return dp[V]
    for i in range(m):
        if V>=coins[i]:
            if (V-coins[i]) in dp:
                a=dp[V-coins[i]]
            else:
                a=minCoins(coins,m,V-coins[i])
            sub=1+a
            if sub!=99999:
                res=min(sub,res)
    dp[V]=res
    return dp[V]

	

# Driver program to test above function
coins = [ 5,11]
m = len(coins)
V = 43
print("Minimum coins required is",minCoins(coins, m, V))


