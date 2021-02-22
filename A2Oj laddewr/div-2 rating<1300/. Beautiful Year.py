year=int(input())
year+=1
def unique(num):


    if len(str(num))==len(set(list(str(num)))):
        return False
    return True




while unique(year):
    year+=1

print(year)