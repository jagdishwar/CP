bin1=bin(2)[2:]
print(bin1)
bin1=bin1[::-1]
added=32-len(bin1)
strmul="0"*(added)
bin1=bin1+strmul
print(bin1,)
bin2=bin1[::-1]
print(len(bin2))
print(int(bin1,base=2))