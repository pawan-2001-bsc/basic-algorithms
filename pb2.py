n=int(input("Enter a number:"))

if n<2:
    print("Not a prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print("Not a prime")
            break
    else:
         print("It is a prime")
