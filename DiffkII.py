list1=[ 34, 63, 64, 38, 65, 83, 50, 44, 18, 34, 71, 80, 22, 28, 20, 96, 33, 70, 0, 25, 64, 96, 18, 2, 53, 100, 24, 47, 98, 69, 60, 55, 8, 38, 72, 94, 18, 68, 0, 53, 18, 30, 86, 55, 13, 93, 15, 43, 73, 68, 29 ]

k=97
            compset=set()
            for i in range(len(list1)):
                if (k-list1[i]) not in compset or (list1[i]-k) not in compset:
                    compset.add(i)
                else:
                    print(1)
            print(0)
