'''Strings are Immutable:
1.Once we declare the string we cannot modify it if we try to modify the string
it will create a new string

2.If new string does not have any reference variable then
it will be removed

3. Python Internally uses String Interning.

4. String interning is the process of checking string intern pool before creating a new object

5. Whenever we want to create new object, Python first will check string intern pool, weather that object already exists or not

when object already exist in the string intern record then address of existing object will be reused.'''
#s1 = 'Kodnest'
#s1 = s1.upper()
#print(s1)

#s1 = 'K'
#print(s1, id(s1))

s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2,id(s2))

print(s1[0])
print(s1[-1])

print('s1 ID of H:',id(s1[0]))
print('s1 ID of o:',id(s1[-1]))

print('s1 ID of W:',id(s2[0]))
print('s2 ID of o:',id(s2[0]))

print('s1 ID of l:',id(s1[2]))
print('s1 ID of l:',id(s1[3]))
print('s2 ID of l:',id(s2[3]))