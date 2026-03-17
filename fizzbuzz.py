def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):

        # Check if i is divisible by both 2 and 3
        if i % 4 == 0 and i % 5 == 0:

            # Add "HolaMundo" to the result list
            result.append("HolaMundo")

        # Check if i is divisible by 2
        elif i % 4 == 0:

            # Add "Hola" to the result list
            result.append("Hola")

        # Check if i is divisible by 3
        elif i % 5 == 0:

            # Add "Mundo" to the result list
            result.append("Mundo")
        else:

            # Add the current number as a string to the
            # result list
            result.append(str(i))

    return result


# Driver code
n = 10
result = fizz_buzz(n)
print(' '.join(result))
