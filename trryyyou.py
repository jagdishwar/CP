A="cool_ice_wifi"
B=["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
            list1 = list(map(str, A.split("_")))
            dict1 = {}
            for i in list1:
                if i in dict1:
                    dict1[i] += 1
                else:
                    dict1[i] = 1
            dict2 = {}

            for i in range(len(B)):
                list2 = list(map(str, B[i].split("_")))
                for j in list2:
                    if j in dict1:

                        if i in dict2:
                            dict2[i] += 1
                        else:
                            dict2[i] = 1

            tuples = sorted(dict2.items(), key=lambda kv: -(kv[1]))
            list4 = []
            for i in tuples:
                list4.append(i[0])
print(list4)