class myClass():
    def method1(seft):
        print "\tHello"

    def method2(self, inputString):
        print "\tSoftware Testing: " + inputString

''' ke thua '''
class child_Class_1(myClass):
   def method3(self):
      #myClass.method1(self)
      print "\tChild_Class_1    Method 3"
   def method4(self):
      print "\tChild_Class_1    Method 4"

class child_Class_2(child_Class_1):
   def method1(seft):
      print "\tHello child_Class_2"
   def method3(self):
      print "\tChild_Class_2    Method 3"


def main():
    ''' myClass '''
    print "myClass:"
    c = myClass()
    c.method1()
    c.method2("Test myClass")

    ''' child_Class_1 '''
    print "\nchild_Class_1:"
    c1 = child_Class_1()
    c1.method1()
    c1.method2('anh tuan')
    c1.method3()
    c1.method4()

    ''' child_Class_2 '''
    print "\nchild_Class_2:"
    c2 = child_Class_2()
    c2.method1()
    c2.method2('pham anh tuan')
    c2.method3()
    c2.method4()


if __name__ == "__main__":
    main()