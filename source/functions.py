def who_is():
   print("Alison")

def display_dat(func):
   def inner():
      print("The current user is: ",end="")
      func()
   return inner

if __name__ == "__main__":
   my_obj =display_dat(who_is)
   my_obj()

