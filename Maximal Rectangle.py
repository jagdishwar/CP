            def histogram(list1):
                area = 0
                stack = [-1]
                list1.append(0)
                for i in range(len(list1)):
                    while stack and list1[stack[-1]] > list1[i]and stack[-1]!=-1:
                        index = stack.pop()
                        height = list1[index]
                        width = i - (stack[-1]) - 1
                        area = max(area, height * width)
                    stack.append(i)
                list1.pop()
                return area
            matrix=[[1,0,0,1,1,1],[1,0,1,1,0,1],[0,1,1,1,1,1],[0,0,1,1,1,1]]
            maxarea=histogram(matrix[0])
            prev=[matrix[0]]

            for row in range(1,len(matrix)):
                export = []
                for col in range(len(matrix[0])):
                    if matrix[row][col]!=0:
                       export.append(matrix[row][col]+prev[0][col])
                    else:
                        export.append(0)
                prev[0]=export
                area=histogram(export)
                maxarea=max(maxarea,area)
            print(maxarea)






