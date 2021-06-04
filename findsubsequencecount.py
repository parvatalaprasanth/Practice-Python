
dp={}
def findSubsequenceCount(S, T,s,t):
    if t==0:
        return 1
    if s==0:
        return 0
    if (s,t) in dp:
        return dp[(s,t)]
    if S[s-1]!=T[t-1]:
        a= findSubsequenceCount(S,T,s-1,t)
    else:
        a= findSubsequenceCount(S,T,s-1,t)+findSubsequenceCount(S,T,s-1,t-1)
    dp[(s,t)]=a
    return dp[(s,t)]

        

# Driver Code
if __name__ == "__main__":
	T = "ge"
	S = "geeksforgeeks"


	print(findSubsequenceCount(S, T,len(S),len(T)))

# This code is contributed
# by vibhu4agarwal
