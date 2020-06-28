happy=2
def recursivedfs(happy):
    if happy == 1:
        return True
    if happy <= 10 :
        return True
    store = 0
    while happy:
        store += (happy % 10) ** 2
        happy = happy // 10
    return recursivedfs(store)


print(recursivedfs(happy))

