word = 'rabbit'
separator = "*" *10
a = "anchor"
b = "bounce"
n = 2

print word.find(word) # 0
print word.find('word') # -1
print 'word'.find('word') # 0
print word.find("") # 0
print word.find(word + '!!!') + 1 #0

print separator

print word.find('hello')
print word.find('ll')
print "apple".find('pp')
print "HELLO".find('hello')

print separator

