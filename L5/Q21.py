def biggest3(a, b, c):
    if a >= b and a >= c:
        return a
    
    if b >= a and b >= c:
        return b
        
    if c >= a and c >= b:
        return c
        

print biggest3(3, 6, 9)
#>>> 9

print biggest3(6, 9, 3)
#>>> 9

print biggest3(9, 3, 6)
#>>> 9

print biggest3(3, 3, 9)
#>>> 9

print('*****************************************')

def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggest (a, b, c):
    return bigger(bigger(a,b), c)

print biggest3(3, 6, 9)
#>>> 9

print biggest3(6, 9, 3)
#>>> 9

print biggest3(9, 3, 6)
#>>> 9

print biggest3(3, 3, 9)
#>>> 9

print('*****************************************')

a=1
b=3
c=4
print max(a, b, c)
