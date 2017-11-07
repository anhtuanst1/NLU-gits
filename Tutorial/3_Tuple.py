tup_1 = ((1,2),(3,4),(5,6))
print "tup_1:\n", tup_1
tup_2 = [(1,2),(3,4),(5,6)]
print "tup_2:\n", tup_2

print "\n\n"

Tup = ('Jan','feb','march')
print "Tup:\t", Tup
Tup = (1,2,3)
print "Tup:\t", Tup
del Tup
#print "Tup:\t", Tup

tup1 = ()
print "tup1:\t", tup1
Tup1 = (1,)
print "Tup1:\t", Tup1

tup1 = ('Pham', 'Anh','Tuan','1995')
tup2 = (1,2,3,4,5,6,7)
print  tup1, "\t", "tup1[0]:", tup1[0], "\t", "tup1[3]:", tup1[3], "\t", type(tup1)
print  tup2, "\t", tup2[1:4]



x = ("Tuan", 22, "Student")    # tuple packing
(name, age, job) = x   # tuple unpacking
print "name:", name
print "age: ",age
print "job: ",job



a=(5,6)
b=(1,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

a=(5,6)
b=(5,4)
if (a>b):print "a is bigger"
else: print "b is bigger"

a=(5,6)
b=(6,4)
if (a>b):print "a is bigger"
else: print "b is bigger\n"


directory = {}
a = "ANH"
b = "TUAN"
value = ("anh", "tuan")
directory[a,b] = value
a = "S"
b = "T"
value = 1
directory[a,b] = value
print "directory:", directory
for a ,b in directory:
    print a, "\t\t", b, "\t\t", directory[a, b], "\t\t", directory.items()
print directory.items()
#print directory


a = {'x':100, 'y':200}
b = a.items()
print "\n", b



x = ("a", "b", "c", "d", "e")
print "x[2:4]:", x[2:4], "\t", "x[:4]:", x[:4], "\n\n"


# all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc
TUP1 = ("Pham", "Tuan", 22, "Sinh vien")
TUP2 = (1,10,5,2,8,0)
#TUP = TUP1
TUP = TUP2
def built_tuple():
    global TUP
    print "all:", "\t\t", all(TUP)
    print "any:", "\t\t", any(TUP)
    print "len:", "\t\t", len(TUP)
    print "enumerate:", "\t\t", enumerate(TUP)
    print "max:", "\t\t", max(TUP)
    #print "min:", "\t\t",, min(TUP)
    print "sorted:", "\t\t", sorted(TUP)
    print "tuple:", "\t\t", tuple(TUP)

built_tuple()