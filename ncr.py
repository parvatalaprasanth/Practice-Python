def solve(n, r):
    # Write your code here
    a=[0]*(n+1)
    a[0],a[1]=1,1
    for i in range(2,n+1):
        a[i]=a[i-1]*i
    ans=a[n]/a[r]
    a=ans/a[n-r]
    return a

print(solve(5,2))
