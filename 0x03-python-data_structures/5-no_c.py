def no_c(my_string):
    # initialize an empty string to store the result
    result = ""
    # loop through each character in the input string
    for char in my_string:
        # if the character is not c or C, append it to the result
        if char not in "cC":
            result += char
    # return the result
    return result
