"""
Question 1

Youu are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""

def alphabet_position(text):
    newStr = []
    for letter in text:
        letter = letter.lower()
        if letter == "a":
            newStr.append("1")
        elif letter == "b":
            newStr.append("2")
        elif letter == "c":
            newStr.append("3")
        elif letter == "d":
            newStr.append("4")
        elif letter == "e":
            newStr.append("5")
        elif letter == "f":
            newStr.append("6")
        elif letter == "g":
            newStr.append("7")
        elif letter == "h":
            newStr.append("8")
        elif letter == "i":
            newStr.append("9")
        elif letter == "j":
            newStr.append("10")
        elif letter == "k":
            newStr.append("11")
        elif letter == "l":
            newStr.append("12")
        elif letter == "m":
            newStr.append("13")
        elif letter == "n":
            newStr.append("14")
        elif letter == "o":
            newStr.append("15")
        elif letter == "p":
            newStr.append("16")
        elif letter == "q":
            newStr.append("17")
        elif letter == "r":
            newStr.append("18")
        elif letter == "s":
            newStr.append("19")
        elif letter == "t":
            newStr.append("20")
        elif letter == "u":
            newStr.append("21")
        elif letter == "v":
            newStr.append("22")
        elif letter == "w":
            newStr.append("23")
        elif letter == "x":
            newStr.append("24")
        elif letter == "y":
            newStr.append("25")
        elif letter == "z":
            newStr.append("26") 
    return " ".join(newStr)


"""
Question 2

Complete the function that takes two integers (a, b, where a < b) and return 
an array of all integers between the input parameters, including them.
"""

def between(a,b):
    arr = []
    for number in range(a,b+1):
        arr.append(number)
    return arr


"""
Question 3

Complete the function that takes a non-negative integer n as input, and 
returns a list of all the powers of 2 with the exponent ranging from 0 
to n ( inclusive ).
"""

def powers_of_two(n):
    arr = []
    for number in range(n+1):
        arr.append(2** number)
    return arr