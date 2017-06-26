a = 5
b = 18

a, b = b, a # a=18 and b=5
a, b = b, a # b=5  and a=18

print a
print b

print "-" * 50
print 'strings'
S=""
Q="potato"

print(Q[0])
#print(S[0]) IndexError: string index out of range
print(S[0:])
