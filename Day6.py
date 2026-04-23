

trans=[]
n =int(input("Enter no of transactions:"))
total=0
risk_range=0
for i in range(n) :
    x=int(input("enter the amount:"))
    total=total+x
    trans.append(x)
count=len(trans)
catag={
    "normal":[],
    "large":[],
    "high_risk":[],
    "invalid":[]
}
for i in trans:
    if i<=0:
        catag["invalid"].append(i)
    elif i<=500:
        catag["normal"].append(i)
    elif i<=2000:
        catag["large"].append(i)
    else:
        catag["high_risk"].append(i)
summary=(total,count)
frequent=False
large_spending=False
suspicious=False
if count>5:
    frequent=True
if total>5000:
  large_spending=True
if len(catag["high_risk"])>=3:
  suspicious=True

if frequent:
  risk_range+=1
if large_spending:
  risk_range+=1
if suspicious:
  risk_range+=1
if risk_range<=1:
    final_risk="Low risk"
elif risk_range==2:
    final_risk="Moderate risk"
else:
    final_risk="High risk"
print("categories :")
print(catag)
print("Total transaction :",total)
print("Number of Transactions :",count)
print("summary :",summary)
print(final_risk)

