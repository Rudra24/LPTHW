phonebook = {'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}

phonebooknew = {'abc': 938477123, 'pqr': 938377456, 'xyz': 947662789}


for a, b in phonebook.iteritems():
    print "Phone number of %s is %d" % (a, b)
print "------------------------"
for name, number in phonebooknew.iteritems():
    print "Phone number of %s is %d" % (name, number)
print "------------------------"
del phonebook['John']
phonebooknew.pop('pqr')

for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
print "------------------------"
for name, number in phonebooknew.iteritems():
    print "Phone number of %s is %d" % (name, number)
print "------------------------"

print "....Exercise work here...."
phonebook['Jake'] = 123456789
del phonebook['Jill']
for name, number in phonebook.iteritems():
    print "Phone number of %s is %d" % (name, number)
