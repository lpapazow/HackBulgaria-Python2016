def sum_of_digits(number):
    sum = 0
    for digit in str(abs(number)):
        sum += int(digit)
    return sum


def to_digits(n):
    result = list()
    for digit in str(n):
        print(digit)
        result.append(int(digit))
    return result



def to_number(digits):
    result = ""
    for digit in digits:
        result += str(digit)
    return result


def count_vowels(str):
    number_of_vowels = 0
    for char in str.lower():
        if char in 'aeiouy':
            number_of_vowels += 1
    return number_of_vowels


def count_consonants(str):
    number_of_consonants = 0
    for char in str.lower():
        if char in 'bcdfghjklmnpqrstvwxz':
            number_of_consonants += 1
    return number_of_consonants


def prime_number(n):
    is_prime = True
    for smaller_numbers in range(2, n - 1):
        if n % smaller_numbers == 0:
            is_prime = False
    return is_prime


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fact_digits(n):
    all_digits = to_digits(n)
    sum_of_factorials = 0
    for digit in all_digits:
        sum_of_factorials += factorial(digit)
    return sum_of_factorials


def fibonacci_nth_member(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_nth_member(n - 2) + fibonacci_nth_member(n - 1)


def fibonacci(n):
    result = [None] * n
    for i in range(0, n):
        result[i] = fibonacci_nth_member(i + 1)
    return result


def fib_number(n):
    return to_number(fibonacci(n))


def palindrome(n):
    if (str(n)[::-1] == str(n)):
        return True
    return False


def char_histogram(string):
    distincts = list(set(string))
    histogram = dict((char, 0) for char in distincts)
    for char in string:
        histogram[char] += 1
    return histogram


def main():
    print(char_histogram("AAAAaaa!!!"))


if __name__ == "__main__":
    main()
