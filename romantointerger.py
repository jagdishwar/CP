def intergerintoroman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    i=0
    str1=''
    while num>0:
        print(i,'i')
        if num-val[i]>=0:
            str1+=syb[i]
            num-=val[i]
        else:
            i+=1


    print(str1)
intergerintoroman(3)

