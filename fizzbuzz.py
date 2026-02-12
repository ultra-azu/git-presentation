def fizz_buzz(n):
    result = []

    for i in range(1, n + 1):

        # Check if i is divisible by both 6 and 7
        if i % 6 == 0 and i % 7 == 0:

            # Add "FizzBuzz" to the result list
            result.append("SixSeven")

        # Check if i is divisible by 6
        elif i % 6 == 0:

            # Add "Fizz" to the result list
            result.append("Six")

        # Check if i is divisible by 7
        elif i % 7 == 0:

            # Add "Fizz" to the result list
            result.append("Seven")

        else:

            # Add the current number as a string to the
            # result list
            result.append(str(i))

    return result


# Driver code
n = 10
result = fizz_buzz(n)
print(' '.join(result))
