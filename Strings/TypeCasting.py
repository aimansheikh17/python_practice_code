#If string is holding integer then it can be converted in to int
a = '30'
b = int(a)
print(b, type(b))

#str to integer conversion is not allowed
x = 'kod'
print(x,type(x))
#y = int(x)
#print(y,type(y))

p = float(input('Enter the float type data'))
print(p, type(p))

# bool()

q = 0
q = bool(q)
print(q, type(q))

'''1. while converting int to bool for all non zero value we will get true
2. while converting int to bool for 0 and empty
we will get false
3 '''