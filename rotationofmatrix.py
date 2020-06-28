            import numpy as np
            matrix=[
                [1, 2],
                [3, 4]
            ]
            matrix2=[]
            lencol,lenrow=len(matrix[0])-1,len(matrix[0])-1


            l=0
            k=len(matrix)-1
            list1=[]
            while l<=lenrow:

                for  i in range(lencol,-1,-1):
                    list1.append(matrix[i][l])
                l+=1

            matrix2=np.array(list1).reshape(lencol+1,lenrow+1)
            print(matrix2)