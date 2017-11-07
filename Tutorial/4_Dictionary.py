Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print (Dict['Tiffany'])


Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
Boy = {'Tim': 18,'Charlie':12,'Robert':25}
Girl = {'Tiffany':22}
print "Boy:", Boy
print "Girl:", Girl, "\n"
studentX = Boy.copy()
studentY = Girl.copy()
print "studentX:", studentX
print "studentY:", studentY, "\n"

# add
Boy.update({"Sarah":9})
print "add:", Boy

# del
del Boy['Charlie']
print "del:", Boy

# Dict.items() -> type: list
print "Students Name: %s" % Dict.items(), "\t\t", type(Dict.items()), "\n"

print "Boy.keys():", Boy.keys(), "\t\t", type(Boy.keys())
print "Dict.keys():", Dict.keys(), "\t\t", type(Dict.keys())
# Kiem tra lan luot tung phan thu trong Boy vs Dict
for key in Boy.keys():
    if key in Dict.keys():
        print True
    else:
        print False
'''
for key in Boy:
    if key in Dict:
        print True
    else:
        print False
'''

# Creat list name, print name + age
print "\n"
Students = Dict.keys()
print "Student:", Students
Students.sort()
print "Students.sort:", Students.sort
for S in Students:
    #print":".join((S,str(Dict[S])))
    print S, ":", str(Dict[S]), "\n"

# len
print "Dict:", Dict
print "Length : %d" % len (Dict)
# type
print "variable Type: %s" %type (Dict)

''' 
    so sanh     '='   ->    0
                '>'   ->    1
                '<'   ->    -1
'''
print "\nBoy : %s" %Boy
print "Girl : %s" %Girl
print cmp(Girl, Boy)

# str()
print "\nprintable string:%s" % str(Dict)