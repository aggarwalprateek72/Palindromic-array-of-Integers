def checkpalindrome(w):
    l= len(w)

    for i in range(l//2):
        if w[i]!=w[l-i-1]:
            return False
    return True

#length of string
n= int(input())
#string input
s= input()
flag=True
for i in range(n, 0, -1):
    if flag==True:
        for j in range(n+1-i):
            ss= s[j:i+j]
            if checkpalindrome(ss):
                print(ss)
                flag=False
    else:
        break

