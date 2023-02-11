def prime(n):
    prime = True
    for i in range(2,n):
        if n%i==0:
            prime = False
    return prime
        
while True:
    n = input("Enter a number: ")
    if prime(int(n))==True:
        print("The number is prime")
    else:
        print("The number is not prime")