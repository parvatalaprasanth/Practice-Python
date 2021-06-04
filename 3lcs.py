# Python program to find
# LCS of three strings

# Returns length of LCS
# for X[0..m-1], Y[0..n-1]
# and Z[0..o-1]
dp={}
def lcsOf3(X, Y, Z, m, n, o):
    if m==0 or n==0 or o==0:
        return 0
    if (m,n,o) in dp:
        return dp[(m,n,o)]
    if X[m-1]==Y[n-1] and Y[n-1]==Z[o-1]:
        a=1+lcsOf3(X, Y, Z, m-1, n-1, o-1)
        return a
    dp[(m,n,o)]=max(lcsOf3(X, Y, Z, m-1, n, o),lcsOf3(X, Y, Z, m, n-1, o),lcsOf3(X, Y, Z, m, n, o-1))

    return dp[(m,n,o)]

# Driver program to test above function

X = 'AGGT12'
Y = 'G12TXAYB'
Z = 'GTT12XBA'

m = len(X)
n = len(Y)
o = len(Z)

print('Length of LCS is', lcsOf3(X, Y, Z, m, n, o))

# This code is contributed by Soumen Ghosh.				
