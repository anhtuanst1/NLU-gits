def func1():
   print "I'm learning Python function\n"
func1()

def square(x):
   s = x * x
   return s
print "square:", square(4), "\n"

def multiply(x,y):
   a = x * y
   return a
print "multiply:", multiply(3,4), "\n"

def multiply_1(x=0,y=0):
   print "x = %d \t\t y = %d" %(x,y)
   a = x * y
   return a
a0 = multiply_1(y=2,x=1)
print "multiply_1:", a0, "\n"

def In(*args):    # Note '*'
   print args
In("hello")
In(1,2,3,4,5)
In ("P","H","A","M")
