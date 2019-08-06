def pattern_pyramid(n):
    for i in range(1,n+1):
        k=n-i
        print(k*" ",i*"*",end="")        
        print("\r")
n=5
pattern_pyramid(n)
