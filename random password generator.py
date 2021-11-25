import random
passwordlength = int(input("Enter the length of password: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
newpassword =  "".join(random.sample(s,passwordlength ))
print ("Your new password:", newpassword)