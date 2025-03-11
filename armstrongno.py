n=int(input("Enter a number:"))

sum=0

temp=n

while temp>0:
    digit=temp%10
    sum=sum+(digit*digit*digit)
    temp=temp//10
   
print(sum)
if (sum==n):
    print("It is an armstrong")
else:
    print("It is not an armstrong")
