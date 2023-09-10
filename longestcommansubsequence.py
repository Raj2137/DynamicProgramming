#Recursion

# def lcs(X, Y, m, n):
    
#     #base case
#     if m==0 or n==0:
#         return 0
#     elif X[m-1]==Y[n-1]:
        
#         return 1+ lcs(X, Y,m-1, n-1)
#     else:
#         return max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))
    
    
    
    
    
    
# print(lcs("yoboyobo", "jobojoboo", 8,9))

#dynamic programming using memorization.

m=8
n= 9
arr= [[-1 for i in range(n+1)]for j in range(m+1)]



def lcs(X, Y, m, n):
    
    #base case
    if m==0 or n==0:
        return 0
    
    if (arr[m-1][n-1] != -1):
        return arr[m-1][n-1]
    elif X[m-1]==Y[n-1]:
        
        arr[m-1][n-1]= 1+ lcs(X, Y,m-1, n-1)
        return arr[m-1][n-1]
    else:
        arr[m-1][n-1]= max(lcs(X, Y, m-1, n), lcs(X, Y, m, n-1))
    
    return arr[m-1][n-1]
    
    
print(lcs("yoboyobo", "jobojoboo", 8,9))

print(arr)