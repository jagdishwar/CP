t=int(input())
str1=input()
r,c,k=map(int,str1.split(" ",3))
def chess_values(r,c,k):
        str14="show me your ass"
        for i in range(1,9):

            if( (r ==1 and c==1) or (r==1 and c==8 )or (r==8 and c==1) or (r==8 and c==8) )and k==i:
                if k==1:
                    return ((k+1)**2)
                if k==2:
                    return

        return str14





print(chess_values(r,c,k))