def is_prime_naive(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True 

number = int(input("напиши число "))
if is_prime_naive(number):
    print("это простое число")

else:
    print("это составное число")