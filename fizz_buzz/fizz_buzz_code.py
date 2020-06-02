def fizz_buzz(number):
    if not number % 3 and not number % 5:
        return 'Fizz Buzz'

    if not number % 3:
        return 'Fizz'

    if not number % 5:
        return 'Buzz' 

    return number


for x in range(1, 100):
    fizz_buzz(x)