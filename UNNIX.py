str1 = "/../"
list1 = str1.split("/")
list2 = []
print(list1)
str2 = ""
for i in list1:
    if i.isalpha():
        list2.append(i)
    if i == '..' and len(list2) > 0:
        list2.pop()
for i in list2:
    str2 += '/' + i
if len(str2) > 0:
    return str2
return '/'