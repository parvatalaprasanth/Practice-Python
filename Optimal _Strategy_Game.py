dp={}
def optimalStrategyOfGame(arr, i,j):
    if i>j:
        return 0
    
    if i==j:
        return arr[i]
    #opponent i+1 or j
    if (i,j) in dp:
         return dp[(i,j)]
    a=arr[i]+min(optimalStrategyOfGame(arr, i+2,j),optimalStrategyOfGame(arr, i+1,j-1))
    #opponent i or j-1
    b=arr[j]+min(optimalStrategyOfGame(arr, i+1,j-1),optimalStrategyOfGame(arr, i,j-2))
    amount=max(a,b)
    dp[(i,j)]=amount
    return amount

arr1= [ 8, 15, 3, 7]
n = len(arr1)
print(optimalStrategyOfGame(arr1, 0,n-1))
dp={}
arr2= [ 2, 2, 2, 2 ]
n = len(arr2)
print(optimalStrategyOfGame(arr2,0, n-1))
dp={}
arr3= [ 20, 30, 2, 2, 2, 10 ]
n = len(arr3)
print(optimalStrategyOfGame(arr3,0, n-1))


