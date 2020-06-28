def displayTable( orders):
    food = set()
    table = set()

    res = [[]]
    for i in orders:
        food.add(i[2])
        table.add(int(i[1]))

    table = list(table)
    table.sort()
    food = list(food)
    food.sort()
    food.insert(0, "Table")
    res[0] = food

    fdict = {}
    for i in range(1, len(food)):
        fdict[food[i]] = i
    print(fdict)
    tdict = {}

    for i in table:
        tdict[i] = [str(i)] + ["0"] * (len(food) - 1)
    print(tdict)

    for i in orders:
        tdict[int(i[1])][fdict[i[2]]] = str(int(tdict[int(i[1])][fdict[i[2]]]) + 1)
        print(tdict)


    for i in table:
        res.append(tdict[i])

orders=[["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
print(orders)
displayTable(orders)
