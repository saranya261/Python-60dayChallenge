n= int(input("Enter the number of requests"))
requests=[]
for i in range (n):
    x=int(input("Enter the number"))
    requests.append(x)

valid = 0
count_l=0
count_m=0
count_h=0
count_i=0
low_demand=[]
moderate_demand=[]
high_demand=[]
invalid_requests=[]
name=input("enter your name :")
print("Taken L is : ",name)
L=0
for i in name:
  if i!=" ":
        L=L+1
pli=L%3
print("pli will be ",pli)
print("Total requests are",n)
for i in range(n):
    if requests[i]<0:

        count_i=count_i+1
        invalid_requests.append(requests[i])
    elif requests[i]==0:

        valid = valid+1
    elif requests[i]>=1 and requests[i]<=20:
        low_demand.append(requests[i])
        valid = valid+1
        count_l=count_l+1
    elif requests[i]>=21 and requests[i]<=50:
        moderate_demand.append(requests[i])
        valid = valid+1
        count_m=count_m+1
    else:
        high_demand.append(requests[i])
        valid=valid+1
        count_h=count_h+1

print("Total valid requests: ",valid)

print("Before personalisation:")
print("low_demand->",low_demand)
print("moderate_demand->",moderate_demand)
print("high_demand ->",high_demand)
print("invalid_requests ->",invalid_requests)
print("After personalisation:")
if pli==0:
    print("The number of requests removed due to pli is",count_l)
    low_demand = []
elif pli==1:
    print("The number of requests removed due to pli is", count_h)
    high_demand = []
else:
    print("The number of requests removed due to pli is", count_l  + count_h)
    low_demand = []
    high_demand = []



print("low_demand->",low_demand)
print("moderate_demand->",moderate_demand)
print("high_demand ->",high_demand)
print("invalid_requests ->",invalid_requests)






