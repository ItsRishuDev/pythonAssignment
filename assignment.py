def removeChar():
    sample_str = "RishabhSoni"
    char = input("Enter character you want to remove from string : ")

    for item in sample_str:
        if item == char:
            sample_str = sample_str.replace(char, "")

    print("Result : ", sample_str)


def countOccurence():
    sample_str = "SampleStringAvailable"
    result = {}
    for char in sample_str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    print("Result is : ", result)


def isAnagram():
    str1 = input("String 1 : ")
    str2 = input("String 2 : ")

    if sorted(str1) == sorted(str2):
        print("String is Anagaram")
    else:
        print("String is not Anagram")


def isPalindrome():
    str1 = input("String 1 : ")
    str1 = str1.lower()
    str2 = str1[::-1]

    if str1 == str2:
        print("String is Palindrome")
    else:
        print("String is not Palindrome")


def vowelConsonant():
    vowel = ["a", "e", "i", "o", "u"]
    consonant = [
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    char = input("Enter Char : ").lower()

    if char in vowel:
        print("Its Vowel")
    elif char in consonant:
        print("Its Consonant")
    else:
        print("Not a character")


def checkDigit():
    digit = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    char = input("Enter Char : ")
    flag = False

    for value in char:
        if value not in digit:
            flag = False
            break
        else:
            flag = True

    if flag:
        print("Value is digit")
    else:
        print("Value is not a digit")


def checkDigit2():
    char = input("Enter Char : ")
    if char.isdigit():
        print("Value is digit")
    else:
        print("Value is not a digit")


def replaceSpace():
    char = input("Enter Char : ")
    sample_str = "This is Sample String"
    new_str = ""

    for value in sample_str:
        if value == " ":
            value = char
            new_str += char
        else:
            new_str += value

    print("Result : ", new_str)


def replaceSpace2():
    char = input("Enter Char : ")
    sample_str = "This is Sample String"
    sample_str = sample_str.replace(" ", char)
    print(sample_str)


def lowerUpper():
    string = input("Enter String : ").upper()
    print("Result : ", string)


def lowerVowelUpper():
    vowel = ["a", "e", "i", "o", "u"]
    string = input("Enter String : ")
    new_str = ""
    for char in string:
        if char in vowel:
            new_str += char.upper()
        else:
            new_str += char
    print("Result : ", new_str)


def missingNumber(arr):
    total = sum(arr)
    actual_total = sum(range(1, len(arr) + 2))
    result = actual_total - total
    print("Missing Number : ", result)


def findDuplicate(arr):
    result_arr = []
    arr_len = len(arr)
    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            if arr[i] == arr[j]:
                if arr[i] not in result_arr:
                    result_arr.append(arr[i])

    print("Duplicate digits : ", result_arr)


def findPair(arr, number):
    result_arr = []
    arr_len = len(arr)
    for i in range(0, arr_len):
        for j in range(i + 1, arr_len):
            if arr[i] + arr[j] == number:
                if [arr[i], arr[j]] not in result_arr:
                    result_arr.append([arr[i], arr[j]])

    print("Pairs : ", result_arr)


def arrCompare(arr1, arr2):
    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    if len_arr1 == len_arr2:
        print("Both array are of same size.")

    else:
        print("Both array are of different size.")


def largestSmallest(arr):
    largest = max(arr)
    lowest = min(arr)
    print(f"Largest Number is {largest} and Smallest Number is {lowest}")


def secondLargest(arr):
    new_arr = sorted(list(set(arr)))
    result = new_arr[-2]
    print("Second largest number : ", result)


def topTwoMaximum(arr):
    new_arr = sorted(list(set(arr)))
    top_first = new_arr[-1]
    top_second = new_arr[-2]
    print(f"Top two maximum number are {top_first} and {top_second}")


def removeDuplicate(arr):
    result_arr = list(set(arr))
    print("Array without duplicate : ", result_arr)


def reverseArray(arr):
    print("Reversed Array")
    for i in range(len(arr) - 1, -1, -1):
        print(arr[i])


def reverseArray2(arr):
    result = arr[::-1]
    print("Revered Array : ", result)


def arrLength(arr):
    count = 0
    for value in arr:
        count += 1

    print("Length of array is : ", count)


def insertLast(arr, value):
    arr += [value]
    print("Result : ", arr)


# Run function by uncommenting them

# removeChar()
# countOccurence()
# isAnagram()
# isPalindrome()
# vowelConsonant()
# checkDigit()
# checkDigit2()
# replaceSpace()
# replaceSpace2()
# lowerUpper()
# lowerVowelUpper()
# missingNumber([1,2,3,5,6,7,8,9])
# findDuplicate([1,2,3,4,5,6,7,3,8])
# findPair([1,2,3,4,5,6,7,8,9,4], 8)
# arrCompare([1,2,4,6],[4,7,4,3,6])
# largestSmallest([1,2,3,4,5,0,77,98])
# secondLargest([1,2,3,4,5,0,98,77])
# topTwoMaximum([3,44,2,5,66,4,33,43,75,43,23,54,34,75])
# removeDuplicate([3,44,2,5,66,4,33,43,75,43,23,54,34,75])
# reverseArray([1,2,3,4,5,6,7,8,9])
# reverseArray2([1,2,3,4,5,6,7,8,9])
# arrLength([1,2,3,4,5,6,7,8,9])
# insertLast([1,2,3,4,5,6,7,8], 9)
