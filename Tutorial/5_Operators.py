x = 5
y = 2
# toan tu so hoc
print "x = ", x
print "y = ", y, "\n"
print "x + y =", x + y
print "x - y =", x - y
print "x * y =", x * y
print "x : y =", float(x) / float(y)
print "x / y =", x / y      # chia lay nguyen
print "x % y =", x % y      # chia lay du
print "x ^ y =", x ** y

# toan tu so sanh
print "\nx = ", x
print "y = ", y
print('x > y  is',x > y)
print('x < y  is',x < y)
print('x == y  is',x == y)
print('x != y  is',x != y), "\n"

print "x is y", x is y
print "x is not y", x is not y

# toan tu gan
print "\nx = ", x
print "y = ", y

c = x + y
print "c = x + y:", c
c += x
print "c += x:", c
c -= y
print "c -= y:", c
c *= y
print "c *= y:", c
c /= y
print "c /= y:", c
c **= y
print "c **= y:", c
c %= y
print "c %= y:", c

# toan tu logic
a = True
b = False
print "\na:", a
print "b:", b
print('a and b is',a and b)
print('a or b is',a or b)
print('not a is',not(a)), "\n"

# toan tu in, not in
x = 4
y = 8
list = [1, 2, 3, 4, 5]
print "x =", x
print "y =", y
print "list =", list
if ( x in list ):           # check x
   print "x thuoc list"
else:
   print "x khong thuoc list"

if ( y not in list ):       # check y
   print "y khong thuoc list"
else:
   print "y thuoc list"

# trinh tu uu tien trong tinh toan
v = 4
w = 5
x = 8
y = 2
z = 0
print "\nv = %d \t w = %d \t x = %d \t y = %d" %(v,w,x,y)
z = (v + w) * x / y
print "Gia tri cua (v + w) * x / y la", z

