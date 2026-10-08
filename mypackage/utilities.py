def greet(name):
    return "Hello, " + name + "! Welcome!"


def factorial(n):
    result = 1

    for number in range(1, n + 1):
        result = result * number

    return result