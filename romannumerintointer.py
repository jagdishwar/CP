def romantointger(rom):
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

        sum1=0
        i=len(rom)-1
        while i>=0:
            k=syb.index(rom[i])
            ele=val[k]
            if i>=0:
                if ele>val[syb.index(rom[i-1])] and i-1>=0:
                    sum1+=ele-val[syb.index(rom[i-1])]
                    i -= 2
                else:
                    sum1+=ele
                    i -= 1


        print(sum1)
romantointger('XX')