dp={}
def longestRepeatedSubSeq(str,m,n):
    if n==0 or m==0:
        return ""
    if (m,n) in dp:
        return dp[(m,n)]
    if str[m-1]==str[n-1] and m!=n:
        return str[m-1]+longestRepeatedSubSeq(str,m-1,n-1)
    dp[(m,n)]= max(longestRepeatedSubSeq(str,m-1,n),longestRepeatedSubSeq(str,m,n-1))
    return dp[(m,n)] 


str = 'AABEBCDD'
l=len(str)
print(longestRepeatedSubSeq(str,l,l)[::-1])
