name=input("enter your full name")
email=input("enter your your email")
mobile=input("enter your mobile number")
Age=int(input("enter your age"))
if (name.count(" ")>=1 and name[0]!=" " and name[len(name)-1]!=" "
        and email[0]!='@' and email.count("@")==1 and email.count(".")==1 and len(mobile)==10 and mobile.isdigit() and mobile[0]!=0 and Age>=18 and Age<=60) :
    print("User Profile is VALID")
else:
    print("User Profile is NOT VALID")