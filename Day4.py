n=int(input("enter the no of  activity scores"))
d=int(input("enter your roll number"))
print("Enter the list of activity scores")
valid=0
count=0
invalid=0
scores=[]
low_risk=[]
medium_risk=[]
high_risk=[]
critical_risk=[]
for i in range(n):
    x=int(input(f"enter the {i+1} activity score "))
    scores=scores+[x]
for i in range(n):
    if scores[i]<0:
        invalid=invalid+1
    elif scores[i]>=0 and scores[i]<=30:
        valid=valid+1
        low_risk=low_risk+[scores[i]]
        if d%5==0 or d%2==0:
            count=count+1
    elif scores[i]>=31 and scores[i]<=60:
        valid=valid+1
        medium_risk=medium_risk+[scores[i]]
    elif scores[i]>=61 and scores[i]<100:
        valid=valid+1
        high_risk=high_risk+[scores[i]]
    else:

        valid=valid+1
        critical_risk=critical_risk+[scores[i]]
print("Registered id is :",d)
print(low_risk)
print(medium_risk)
print(high_risk)
print(critical_risk)
print("After personalisation :")


if d%5==0 or d%2==0:
    low_risk=[]
print(low_risk)
print(medium_risk)
print(high_risk)
print(critical_risk)
print("Total valid entries :",valid)
print("Total ignored entries :",invalid)
print("Removed due to personalisation :",count)





