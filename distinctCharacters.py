# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Author: KharelUtsav


def distinctCharacters(string): #Argument type: String, Return type: String
    """
    distinctCharacters function takes a string as an argument and prints 
    the distinct characters in the given string. For loop is run on string
    to get individual characters of string and assigned to variable named 
    new.
    On every iteration, it is checked whether the current element is
    present in new variable and added to new variable only if character is
    new to string.
    The function returns the string with comma separated distinct_string 
    enclosed in curly brackets.
    """
    distinct_string = ""
    #Iterating through the given string.
    for character in string:
    #Checking and concatenating unique/distinct characters to new 
        distinct_string = distinct_string if character in distinct_string \
            else distinct_string + character
    #Returning comma separated distinct characters inside curly braces.
    return print("{" + ",".join(distinct_string) + "}")

#Test case: 1
input1 = "cricket"
distinctCharacters(input1)

#Test case: 2
input2 = "developer"
distinctCharacters(input2)

