import re

def email_check(email):
 rexge= r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

 if re.match(rexge,email):
    return True
 else:
    return False
def password_check(password):
 char= r'^[A-Z][a-z0-9._%$#@%&]{8,}$'
 min_len=8

 if re.match(char,password):
    return True
 elif len(password)>= min_len:
   return True
 else:
    return False



def main():
 max_tries=4
 Tries=-1
 while Tries<max_tries:
  email=input("Enter Your Email: ").strip()
  if email_check(email):
   password=input("Enter Your Password : ").strip()
   if password_check(password):
    print( "Welcom To Your Email")
    break
   else:

    Tries+=1
    print( f"Wrong Password You Have {'Last'if Tries==max_tries else max_tries-Tries} chance left")
  else:
    Tries+=1
    print( f"Wrong Email You Have {'Last'if Tries==max_tries else max_tries-Tries} chance left")
 if Tries==max_tries:
   print("You have used all your attempts. Please try again later.")
print(main())


    
    
    


 