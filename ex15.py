__author__ = 'rudragouda'


from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % txt
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(filename)

print txt_again.read()


# import random
# arr = []
# arr=random.sample(range(1, 2000), 50)
#
#
# print arr
#
# for i, r in enumerate(arr):
#     if r < 10:
#         arr[i] = '0'+ str(r)
#     if int(arr[i]) < 100:
#         arr[i] = '0'+ str(arr[i])
#     if int(arr[i]) < 1000:
#         arr[i] = '0'+ str(arr[i])
#         print arr[i]
#     if arr[i] > 999:
#         arr[i] = str(arr[i])
# print arr

# import string
# import random
#
#
# def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))
# l=[]
# for i in xrange(10000):
#     id_n = id_generator()
#     if id_n not in l:
#         l.append(id_n)
#     else:
#         print "id existing..."
# print l
# mystr = string.ascii_uppercase
# print mystr
# mydig = string.digits
# print mydig
# strdig = string.ascii_uppercase + string.digits
# print strdig
# id_generator(3, "6793YUIO")
