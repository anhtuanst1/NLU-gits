def main():
   ''' while loop'''
   x = 0
   while (x < 4):
      print x
      x +=1

   print "\n"
   ''' for loop '''
   for i in range(20):
      if i == 11:
         break          # break
      if i % 2 == 0:
         continue       # continue
      print i

   print "\n"
   for i in ('ABC','123'):
      print i

   ''' for loop in string '''
   print "\n"
   Months = ["Jan","Feb","Mar","April","May","June"]
   for m in Months:
      print m

   print "\n"
   for i, m in enumerate(Months):      # enumerate
      print i, m


if __name__ == "__main__":
   main()