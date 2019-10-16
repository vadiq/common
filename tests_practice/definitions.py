from string import ascii_lowercase


def task1_common_elements(a, b):
    """
    Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates).
    """
    c = []
    for i in set(a):
        if i in set(b):
            c.append(i)
    if not c:
        return None
    else:
        return c


def task2_letter_times(s):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    letter = 'a'
    count = 0
    for i in str(s):
        if i == letter:
            count += 1
    return count


def task3_is_power(num):
    """
    Write a Python program to check if a given positive integer is a power of three
    Input : 9
    Output : True
    """
    power = 3
    while num > power:
        num /= power
    return num == power


def task4_add_repeatedly(num):
    """
    Write a Python program to add the digits of a positive integer
    repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 2: 1 + 4 = 5
    """
    while len(str(num)) != 1:
        num = sum([int(i) for i in str(num)])
    return num


def task5_push_zeros(a):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0, 2, 3, 4, 6, 7, 10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    for i in a:
        if i == 0:
            a.remove(i)
            a.append(0)
    return a


def task6_arithmetic_progression_check(a):
    """
    Write a Python program to check a sequence of numbers is an
    arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence is
    a sequence of numbers such that the difference between the
    consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ...
    is an arithmetic progression with common difference of 2.
    """
    # властивість арифметичної прогресії (знаходження суми елементів)
    arithmetic_sequence_sum = (a[0] + a[-1]) / 2 * len(a)
    return sum(a) == arithmetic_sequence_sum


def task7_unique_number(a):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    if len(a) == 1:
        return a[0]
    elif len(a) == 0:
        return None
    else:
        # ======= main code
        b = []
        for i in a:
            c = a.copy()
            a.remove(i)
            if i not in a:
                b.append(i)
            a = c
        # ===================
        if len(b) == 1:
            return b[0]
        elif len(b) == 0:
            return None
        else:
            return b


def task8_missing_number(a):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    check_list = list(range(1, max(a) + 1))
    result = list(set(check_list) - set(a))
    if len(result) == 1:
        return result[0]
    elif len(result) == 0:
        return None
    else:
        return result


def task9_find_before_tuple(a):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1, 2, 3, (1, 2), 3]
    Output: 3
    """
    for i in a:
        if type(i) == tuple:
            return a[a.index(i) - 1]


def task10_string_reversed(a):
    """
    Write a program that will take the str parameter being passed and
    return the string in reversed order.
    For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    # first attempt
    # a = list(a)
    # a.reverse()
    # return "".join(a)
    # but then I googled about slicing and reversed list
    return a[::-1]


def task11_time_converter(num):
    """
    Write a program that will take the num parameter being passed and
    return the number of hours and minutes the parameter converts to
    (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    if num < 0:
        raise ValueError
    h = num // 60
    m = num % 60
    result = str(h) + ':' + str(m)
    return result


def task12_largest_word(text):
    """
    Write a program that will take the parameter being passed and
    return the largest word in the string. If there are two or more
    words that are the same length, return the first word from the string with that length.
    Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love
    """
    if not text:  # check if empty
        return None
    if type(text) is str:  # check if type is string and not empty
        max_word = max([''.join(char for char in word if char.isalpha())
                        for word in text.split(' ')], key=len)
        return max_word
    raise ValueError


def task13_words_backward(text):
    """
    Write a program (using functions!) that asks the user for
    a long string containing multiple words.
    Print back to the user the same string, except with the words in backwards order.
    For example:
    Input: My name is Michele
    Output: Michele is name My
    """
    if not text:
        return None
    if type(text) is str:
        text = text.split(' ')
        text.reverse()
        text = ' '.join(text)
        return text
    raise ValueError


def task14_fibonacci():
    """
    Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
    Take this opportunity to think about how you can use functions.
    Make sure to ask the user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonacci sequence is a sequence of numbers where
    the next number in the sequence is the sum of the previous two numbers in the sequence.
    The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    num = int(input('Enter item counts for Fibonacci numbers\n'))
    if num == 1:
        return [1]
    elif num > 1:
        lst = [1, 1]
        i = 1
        while i < (num - 1):
            j = lst[i] + lst[i - 1]
            lst.append(j)
            i += 1
        return lst


def task15_even_only(a):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes
    a new list that has only the even elements of this list in it.
    """
    if type(a) is list:  # check if variable is list
        if a:  # check if list is not empty
            lst = [i for i in a if i % 2 == 0]
            if lst:  # check if result is not empty
                return lst
            else:
                return "No even numbers"
    raise ValueError


def task16_sum_up_until():
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    num = int(input('Enter how many numbers to sum up\n'))
    result = 0
    for i in range(num + 1):
        result += i
    return result


def task17_factorial(num):
    """
    Write a program that will take the parameter being passed and return the factorial of it.
    For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24.
    """
    if type(num) is int:  # check if parameter is integer
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result
    raise ValueError


def task18_letter_replacement(text):
    """
    Write a program that will take the str parameter being passed and
    modify it using the following algorithm.
    Replace every letter in the string with the letter following it
    in the alphabet (i.e. c becomes d, z becomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and
    finally return this modified string.
    Input: abcd
    Output: bcdE
    """
    if type(text) is str:  # check if text is string
        if text:  # check if not empty
            text2 = []
            for i in text:
                new_i_index = ascii_lowercase.index(i) + 1
                new_i = ascii_lowercase[new_i_index]
                if new_i in 'aeiou':
                    new_i = new_i.upper()
                text2.append(new_i)
            return ''.join(text2)
    raise ValueError


def task19_alpha_order(text):
    """
    Write a program that will take the str string parameter
    being passed and return the string with the letters in alphabetical order
    (i.e. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    if type(text) is str:  # check if text is string
        if text:  # check if not empty
            return ''.join(sorted(text))
    raise ValueError


def task20_num2_check(a, b):
    """
    Write a program that will take both parameters being passed and
    return the true if num2 is greater than num1, otherwise return the false.
    If the parameter values are equal to each other then return the string -1
    """
    if type(a) and type(b) is int:  # check if parameters are integer
        if a == b:
            return '-1'
        return a < b
    raise ValueError
