def madianofarray():
    list1=[1,3,6,90]
    list2=[11,23,34,67]
    x=len(list1)
    y=len(list2)
    l=0
    h=x-1
    while h>=l:
        partitionx=(h+l)//2
        partitiony=((x+y+1)//2)-partitionx
        if partitionx-1==0:
            partitionxleft = float('-inf')
        if partitionx-1!=0:
            partitionxleft=list1[partitionx-1]
        if partitionx==x:
            partitionxright=float('inf')
        if partitionx!=x:
            partitionxright=list1[partitionx]
        if partitiony-1==0:
            partitionyleft = float('-inf')
        if partitiony-1!=0:
            partitionyleft=list2[partitiony-1]
        if partitiony==y:
            partitionyright=float('inf')
        if partitiony!=y:
            partitionyright=list2[partitiony]



        if partitionxright>=partitionyleft and partitionyright>=partitionxleft:
            if (x+y)%2==0:
                print(1)
                print((max(partitionxleft,partitionyleft),min(partitionyright,partitionxright)))
            else:
                print(max(partitionyleft,partitionyleft))
            break
        elif partitionxleft>partitionyright:
            h=partitionx-1
        else:
            l=partitionx+1


madianofarray()