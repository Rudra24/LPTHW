__author__ = 'rudragouda'

i = 1
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
    print "------iterating the loop------"

print "------Exit the Loop------"
print "The numbers: "

for num in numbers:
    print num
