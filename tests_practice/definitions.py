from string import ascii_lowercase


def task1_common_elements(list1, list2):
    """
    Take two lists, say for example these two:
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list that contains only
    the elements that are common between the lists (without duplicates).
    """
    try:
        result_list = []
        for elem in set(list1):
            if elem in set(list2):
                result_list.append(elem)
        return result_list
    except TypeError:
        raise TypeError


def task2_letter_times(text):
    """
    Return the number of times that the letter “a” appears anywhere in the given string
    Given string is “I am a good developer. I am also a writer” and output should be 5.
    """
    letter = 'a'
    count = 0
    for abc in str(text):
        if abc == letter:
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


def task5_push_zeros(input_list):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0, 2, 3, 4, 6, 7, 10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    for elem in input_list:
        if elem == 0:
            input_list.remove(elem)
            input_list.append(0)
    return input_list


def task6_arithmetic_progression_check(list_input):
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
    difference = list_input[1] - list_input[0]
    for i in range(2, len(list_input)):
        if difference != list_input[i] - list_input[i - 1]:
            return False
        i += 1
    return True


def task7_unique_number(lst):
    """
    Write a Python program to find the number in a list that doesn't occur twice.
    Input : [5, 3, 4, 3, 4]
    Output : 5
    """
    unique = []
    for elem in lst:
        check_list = lst.copy()
        lst.remove(elem)
        if elem not in lst:
            unique.append(elem)
        lst = check_list
    return unique


def task8_missing_number(num):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    check_list = list(range(1, max(num) + 1))
    result = list(set(check_list) - set(num))
    return result


def task9_find_before_tuple(lst):
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1, 2, 3, (1, 2), 3]
    Output: 3
    """
    result = 0
    for elem in lst:
        if isinstance(elem, tuple):
            result = lst[lst.index(elem) - 1]
            break
    return result


def task10_string_reversed(text):
    """
    Write a program that will take the str parameter being passed and
    return the string in reversed order.
    For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    return text[::-1]


def task11_time_converter(num):
    """
    Write a program that will take the num parameter being passed and
    return the number of hours and minutes the parameter converts to
    (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    if num < 0:
        raise ValueError
    hour = num // 60
    minute = num % 60
    result = str(hour) + ':' + str(minute)
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
    if isinstance(text, str) and text:  # check if type is string and not empty
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
    if isinstance(text, str) and text:
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
    lst = [1, 1]
    i = 1
    while i < (num - 1):
        j = lst[i] + lst[i - 1]
        lst.append(j)
        i += 1
    return lst


def task15_even_only(lst):
    """
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes
    a new list that has only the even elements of this list in it.
    """
    if isinstance(lst, list) and lst:  # check if list and is not empty
        return [elem for elem in lst if elem % 2 == 0]
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
    if isinstance(num, int):
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
    if isinstance(text, str) and text:  # check if text is string and not empty
        new_text = []
        for char in text:
            new_char_index = ascii_lowercase.index(char) + 1
            new_char = ascii_lowercase[new_char_index]
            if new_char in 'aeiou':
                new_char = new_char.upper()
            new_text.append(new_char)
        return ''.join(new_text)
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
    if isinstance(text, str) and text:  # check if text is string
        return ''.join(sorted(text))
    raise ValueError


def task20_num2_check(param1, param2):
    """
    Write a program that will take both parameters being passed and
    return the true if num2 is greater than num1, otherwise return the false.
    If the parameter values are equal to each other then return the string -1
    """
    if isinstance(param1, int) and isinstance(param2, int):  # check if parameters are integer
        if param1 == param2:
            return '-1'
        return param1 < param2
    raise ValueError
