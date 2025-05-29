
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# Example
print(sum_of_digits(1234))  # Output: 10
