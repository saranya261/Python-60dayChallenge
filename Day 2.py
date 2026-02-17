
studentID=input("Enter  Student ID")
Email=input("Enter  Email")
Password=input("Enter  Password")
Referral=input("Enter  Referral code")
if (studentID[0]=='C'and studentID[1]=='S'and studentID[2]=='E' and studentID[3]=='-'
        and studentID[4].isdigit() and studentID[5].isdigit() and studentID[6].isdigit() and
        len(studentID)==7 and Email.count('@')>=1 and Email[0]!='@' and Email[len(Email)-4]=='.'
        and Email[len(Email)-3]=='e' and Email[len(Email)-2]=='d' and Email[len(Email)-1]=='u' and
        len(Password)>=8 and Password[0].isupper()  and (Password.count('0') >=1 or Password.count('1')>=1
        or Password.count('2')>=1 or Password.count('3')>=1 or Password.count('4') >=1 or
        Password.count('5') >=1 or Password.count('6') >=1 or Password.count('7')>=1 or Password.count('8')>=1
        or Password.count('9')>=1 )and Referral[0]=='R'and Referral[1]=='E'and Referral[2]=='F'and Referral[3].isdigit()
        and Referral[4].isdigit() and Referral[5]=='@'):
    print("APPROVED")
else:
    print("REJECTED")