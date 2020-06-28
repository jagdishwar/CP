import re
##################### making icon ####################

p=input('enter the your password ')
while True:
    if (len(p)<6)or len(p)>16:
        print('Invalid Password')
        print('try to improve')
        break
    elif not re.search('[a-z]',p):
        print('sorry,Invalid password\n')
        print('please add some alphabets')
        break
    elif not re.search('[0-9]',p):
        print('sorry,Invalid password')
        print('please add some numbers')
        break
    elif not re.search('[A-Z]',p):
        print('sorry,Invalid password')
        print('add some capital letters')
        break
    elif not re.search('[$#@]',p):
        print('sorry,Invalid password, your are missing something')
        print('try some #,$,@ letters')
        break
    else:
        print('Great!!! your password is valid')
        break
