            list4=[]
            for i in range(3):
                lst = [0 for i in range(3)]
                list4.append(lst)
            print(list4)

            t = 0
            b = 3- 1
            l = 0
            r = 3- 1
            dir = 0
            counter=1
            while(t <= b and l <= r):
                        if(dir == 0):
                            for i in range(l,r+1):
                                list4[t][i]=counter
                                counter+=1
                            t += 1
                        elif(dir == 1):
                            for i in range(t,b+1):
                                list4[i][r]=counter
                                counter+=1
                            r -= 1
                        elif(dir == 2):
                            for i in range(r,l-1,-1):
                                list4[b][i]=counter
                                counter+=1
                            b -= 1
                        elif (dir == 3):
                            for i in range(b,t-1,-1):
                                list4[i][l]=counter
                                counter+=1
                            l += 1
                        dir = (dir + 1) % 4

            print(list4)
