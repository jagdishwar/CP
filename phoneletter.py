phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

def dfsforphoneletter(combination,digits,output):
    if len(digits) == 0:
        output.append(''.join(combination))

        return

    else:
        for letter in phone[digits[0]]:
            combination.append(letter)
            dfsforphoneletter(combination,digits[1:],output)
            combination.pop()


output=[]
digits='2793'
dfsforphoneletter([],digits,output)
print(output)