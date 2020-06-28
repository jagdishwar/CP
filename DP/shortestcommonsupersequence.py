list1=[ "cpsklryvmcp", "nbpbwllsrehfmx", "kecwitrsglre", "vtjmxypu" ]

strx=list1[0]
stry=list1[1]
def scs(strx,stry):
        t=[[0 for i in range(len(stry)+1)] for j in range(len(strx)+1)]
        for i in range(1,len(strx)+1):
            for j in range(1,len(stry)+1):
                if strx[i-1]==stry[j-1]:
                    t[i][j]=1+t[i-1][j-1]
                else:
                    t[i][j]=max(t[i-1][j],t[i][j-1])

        maxcommon=t[-1][-1]

        i=len(strx)
        j=len(stry)
        result=""
        while i>0 and j>0:
            if strx[i-1]==stry[j-1]:
                result+=strx[i-1]
                i-=1
                j-=1
            else:
                if t[i][j-1]>t[i-1][j]:
                    result+=stry[j-1]

                    j-=1
                else:
                    result+=strx[i-1]

                    i-=1

        while i>0:
            result+=strx[i-1]
            i-=1
        while j>0:
            result+=stry[j-1]
            j-=1
        return result
result=scs(strx,stry)[::-1]
print(result)
for i in range(2,len(list1)):

    result=scs(result,list1[i])[::-1]
    print(result)
pr

