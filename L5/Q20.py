def is_friend(name):
    if name[0] == 'D':
        return True
    if name[0] == 'N':
        return True
    return False

print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False

#...........................

def is_friend2(name):
    return name[0] == 'D' or name[0] == 'N'

print is_friend2('Nicole')
print is_friend2('Dana')
print is_friend2('Freddy')

#...........................

print '----True or False----'
print False or False
#>>> False

print True or True
#>>> True

print True or False
#>>> True

print False or True
#>>> True

print True or anything #>>> True
print anything or True #>>> NameError: name 'anything' is not defined
print False or anything #>>> NameError: name 'anything' is not defined
