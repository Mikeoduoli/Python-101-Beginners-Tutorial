def checkFibonacci(number):
    if number < 0:
        return False

    a, b = 0, 1
    while b < number:
        a, b = b, a + b

    return b == number

checkFibonacci(24);
checkFibonacci(8);