def main():
   x = 8
   y = 4
   if (x > y):
      st = "x lon hon y"
   elif (x < y):
      st = "x nho hon y"
   else:
      st = "x bang y"
   print st

   ''' price_shipping '''
   total = 50
   country = "US"
   #country = "AU"
   if country == "US":
      print "US"
      if total <= 50:
         print "Shipping Cost is  $50"
      elif total <= 100:
         print "Shipping Cost is $25"
      elif total <= 150:
         print "Shipping Costs $5"
      else:
         print "FREE 1"
   elif country == "AU":
      print "AU"
      if total <= 50:
         print "Shipping Cost is  $100"
      else:
         print "FREE 2"
   else:
      print "FREE 3"

if __name__ == "__main__":
   main()