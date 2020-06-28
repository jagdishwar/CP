def word_count_engine(document):
    list4 = []
    list1 = document.lower().split(' ')

    occurrence_dict = {}

    for idx, i in enumerate(list1):
        str2 = ''
        for j in i:
            if ord('a') <= ord(j) <= ord('z'):
                str2 += j
        list4.append(str2)
        occurrence_dict[i] = idx
    dict1 = {}
    for i in list4:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1

    output = [[word, count] for word, count in dict1.items()]
    # O(n logn)
    output.sort(key=lambda x: (x[1], -occurrence_dict[x[0]]), reverse=True)
    for i in range(len(output)):
        output[i][1] = str(output[i][1])
    return output







