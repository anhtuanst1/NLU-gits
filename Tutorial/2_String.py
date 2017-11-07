print 'R\n'
print '\nr'

''' Gan chuoi '''
name = 'Anhtuanst'
number = 1
print'%s abc %d' % (name,number)

''' Ghep chuoi '''
x="Anhtuan"
y="1"
print x+y

''' Lap lai chuoi '''
x="Anhtuan"
y="st1"
print x*2 + " " + y*2

''' Cat chuoi '''
x = "Pham Anh Tuan"
print x[:4]
print x[0:4] + " Tuan"

''' Thay the '''
oldstring = 'Pham A Tuan'
newstring = oldstring.replace('A', 'Anh')
print oldstring, "\t\t", newstring

''' Chuyen chu thuong thanh chu in hoa '''
string="anhtuanst1"
print string.upper()

''' Viet in hoa ki tu dau '''
string="pham anh tuan"
print string.capitalize()

''' De ki tu ":" giua tung ki tu trong chuoi '''
print":".join("anhtuan")

''' Chuoi dao nguoc '''
string="12345"
print string, "\t", ''.join(reversed(string))

''' Cat chuoi boi ' ' -> dau ra la 1 mang '''
word="pham anh tuan"
mang = word.split(' ')
print "mang ' ': ", mang
print "mang[1]: ", mang[1]
print "mang 'a': ", word.split('a')

x = "pham anh tuan"
x1 = x.replace("anh","Python")
print "x: ", x, "\t", "x1: ", x1, "\t", "x: ", x

