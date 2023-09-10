# def fabnoci(n, pre=0, res=1):
#     r= pre+res
#     n-=1
#     if n>1:
#         pre= res
#         res= r
#         fabnoci(n,pre, res)
#     print(r)
#     return r

# '''Main recursion'''


# def fab(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     if n > 1:
#         return fab(n-1)+fab(n-2)

''' Using top-down approch'''
arr= [0 for i in range(100)]
def fabo(n):
    
    if n<=1:
        return n
    if arr[n]!=0:
        return arr[n]
    else:
        arr[n]= fabo(n-1)+fabo(n-2)
    return arr[n]
print(fabo(9))
  






