def permute(arr):
    if len(arr)<2:
        return arr
    
    inverse=len(arr)-2
    
    while inverse>=0 and arr[inverse]>=arr[inverse+1]:
        inverse-=1
    
    if inverse<0:
        return 
    
    for i in reversed(range(inverse, len(arr))):
        if arr[i]>arr[inverse]:
            arr[i], arr[inverse]=arr[inverse],arr[i]
            break
    arr[inverse+1:]= reversed(arr[inverse+1:])
    return arr



n,k= map(int, input().split())

for _ in range(k):
    l= list(map(int, input().split()))

    print(permute(l))
