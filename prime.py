# Check whether given number is prime or composite
n=int(input("\nEnter Your Number:"))
i=2
is_prime=True
while i <=n/2:
    if (n %i==0):
        is_prime=False
    i=i+1
if is_prime: print(n,"is a prime Number")
else:
    print(n,"is composite Number")







