import re

# Example of w+ and ^ Expression
x = "Tuan, education is fun"
print "x = ", x
r1 = re.findall(r"^\w", x)      # chay tu ki tu bat dau
print r1
r1 = re.findall(r"^\w+", x)
print r1, "\n"

# Example of \s expression in re.split function
print "\s: ", (re.split(r'\s','we are'))
print "\d: ", (re.split(r'\d','we are'))
print "\D: ", (re.split(r'\D','we are'))
#print "$: ", (re.split(r'$','we are'))
print ".b: ", (re.split(r'.b','we are _b'))

print '\ns: ', (re.split(r's','split the words'))
print 't: ', (re.split(r't','split the words'))
print 'd: ', (re.split(r'd','split the words'))

print "\n"
# Use re.match()
list = "guru99 get", "guru99 give", "guru99 hi", "hi guru99"
for element in list:
    z = re.match("(g\w+)\W(h\w+)", element)     # chay tu ki tu g... h...
    if z:
        print(z.group())

print "\n"
# Use re.search()       Tim kiem tu trong 1 chuoi
patterns = [ 'tuan', 'st1' ]
text = 'pham anh tuan'
for pattern in patterns:
 	print 'Looking for "%s" in "%s" ->' % (pattern, text),
	if re.search(pattern,  text):
	    print 'found a match!'
	else:
	    print 'no match'

print "\n"
# Use re.findall()
abc='guru99@google.com, careerguru99@hotmail.com, users@yahoomail.com'
emails = re.findall(r'[\w\.-]+@[\w\.-]+', abc)
print "emails: ", emails
#print "emails[0]: %s \t emails[1]: %s \t emails[2]: %s " %(emails[0],emails[1],emails[2])
for email in enumerate(emails):
    print email

print "\n"
# Example of re.M or Multiline Flags        (re.I, re.S, re.U, re.L)
xx = """pham
anh
tuan"""
k1 = re.findall(r"^\w", xx)
k2 = re.findall(r"^\w", xx, flags = re.M)

print "xx: ", xx
print "k1: ", k1
print "k2: ", k2




