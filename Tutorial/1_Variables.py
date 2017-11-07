a = 100
print a, type(a)


f = 99
print f, type(f)
f = "Pham Anh Tuan"
print f, type(f)


a = "Tuan"
b = 99
print a + str(b)
print "Tuan", 99


print "\n", "no global"
''' no global '''
f = "Pham Tuan"
print "f.1 ", "\t", f, "\t", type(f)

def Change_0():
    f = "Tuan"
Change_0()
print "f.2", "\t", f, "\t", type(f)


print "\n", "global"
''' global '''
f = "Pham Tuan"
print "f.1 ", "\t", f, "\t", type(f)

def Change():
    global f
    f = "Tuan"
Change()
print "f.2", "\t", f, "\t", type(f)


''' delete var '''
z = 123
print z
del z
print z
