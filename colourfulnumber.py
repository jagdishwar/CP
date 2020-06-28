                def combination(num,combinationn,output):
                    if len(combinationn)>1 :
                        output.append(''.join(combinationn[:]))
                    for i in range(len(num)):
                        combinationn.append(num[i])
                        combination(num[i+1:],combinationn,output)
                        combinationn.pop()


                output=[]
                num='3263'
                combination(num,[],output)

                print(output)
                dictlist=dict()
                for i in output:
                    mula=1
                    for j in i:
                        mula*=int(j)
                    if mula in dictlist:
                        dictlist[mula]+=1
                    else:
                        dictlist[mula]=1

                for key,value in dictlist.items():
                    if value>1:
                        return 0

                return 1


