def pow(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            xx=pow(x,n//2)
            ans=xx*xx
            if  n&1:
                ans*=x
            return ans
if n<0:
    return 1/pow(x,-n)
return (pow(x,n))

##iterative
flag=0
if n<0:
            n=-n
            flag=1
        
        ans=1
while n>0:
            if n&1:
                ans*=x
                n-=1
            x*=x
            n//=2
if flag==1:
    return 1/ans
return(ans)
   
    
