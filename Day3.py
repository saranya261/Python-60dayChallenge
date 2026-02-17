N=int(input("enter no of students:"))
marks=[0]*N
count=0
count_f=0
roll=int(input("Enter your 2-digit roll for personalisation:"))

digit=roll%10

for i in range(len(marks)):
    marks[i]=int(input("enter marks:"))
    digi=marks[i]%10
    if digi==digit:
        if marks[i]>=95 and marks[i]<=100:
           past=marks[i]
           marks[i]=100
           print(f"the {past}  are increased to {marks[i]}due to personalisation")
        else:
          past = marks[i]
          marks[i]=marks[i]+5
          print(f"the {past}  are increased to {marks[i]}due to personalisation")
    if marks[i]>=90 and marks[i]<=100:
        print(f"{marks[i]}->Excellent")
        count=count+1
    elif marks[i]>=75 and marks[i]<=89:
        print(f"{marks[i]}->Very good")
        count=count+1
    elif marks[i]>=60 and marks[i]<=74:
        print(f"{marks[i]}->Good")
        count=count+1
    elif marks[i]>=40 and marks[i]<=59:
        print(f"{marks[i]}->Average")
        count=count+1
    elif marks[i]>=0 and marks[i]<=39:
        print(f"{marks[i]}->Fail")
        count=count+1
        count_f=count_f+1
    else:
        print(f"{marks[i]}->Invalid")

print("Total valid students :",count)
print("Total Failed students :",count_f)

