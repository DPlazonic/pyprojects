print("Hey! This is unit converter, you can convert kilometers into miles")

while True:
   km = float(input("Enter value in km: "))

   miles = km * 0.621371

   print("{0} kilometers is {1} miles".format(km, miles))

   try_again = input("Another one? (y/n)")
   
   if try_again.lower() == "n":
      print("Goodbeye!")
      break 