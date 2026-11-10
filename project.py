def my_factorial(n):
    if n < 0:
        raise ValueError("Число не может быть отрицательным")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result


def my_start_str():
    return "Hello world!"
