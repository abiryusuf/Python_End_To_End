
def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, n):
        if n%i == 0:
            return "It's not prime"
        else:
            return "It's prime"
x = int(input("Enter the number: "))

print(isPrime(x))