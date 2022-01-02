# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Author: KharelUtsav


#Arrays containing word representation of necessary numbers.
high = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']

#Numbers containing tens excluding hundred.
tens = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']

#Numbers between ten and twenty
teens = ['', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']

#Numbers below ten
below_ten = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ']

def integerToEnglishCurrency(num): #Argument type: non-negative Number/Integer, Return type: String
    """
    integerToEnglishCurrency function takes num parameter of type integer. It checks if number is 0 and returns Zero if true.

    Number is converted string and necessary number of 0's are added to convert strings length into multiple of three.

    Loop through modified String in length of three. Increment count values by 3 and assign converted string to converted variable.

    Return string representation of given currency.

    """

    #If num is 0: return Zero
    if num == 0:
        return 'Zero'
        #Return to caller

    #Else: number to string
    numStr = str(num)

    #If: String.length % 3 not equal to 0 
    if 3-(len(numStr) % 3) != 3:  
        #String => (('0' * n) + String) % 3 equals 0
        numStr = ((3-(len(numStr) % 3)) * '0') + numStr
    
    #Divide length of String by three for looping.
    length = len(numStr) // 3
    
    #Container to store converted string
    converted = ""

    #Count
    count = 0
    
    #Iterate through range of length (i.e. 0, 1, ..., length-1)
    for i in range(length):
        #Number in hundreds position
        one = int(numStr[count + 0])
        #Number in tens position
        two = int(numStr[count + 1])
        #Number in one position
        three = int(numStr[count + 2])

        if one == 0 and two == 0 and three == 0:
            count += 3
            continue
        
        #Hundred converstion
        converted += below_ten[one]

        #Concats string Hundred to converted variable only if hundreds position is not equal to zero.
        if one > 0:
            converted += 'Hundred '
        
        #Else if tens position is 1, then just concat string from teens array with converted (i.e '', 'Eleven', ..., 'Nineteen'). 
        if two == 1:
            converted += teens[three]
        
        #Else if tens position is not 1, then concat string from tens array
        # and below_ten array(i.e '', 'One', ..., 'Nine') with converted (i.e '', 'Eleven', ..., 'Nineteen'). 
        else:
            converted += tens[two] + below_ten[three]

        #High values(i.e '', 'Thousand', ..., 'Trillion')    
        converted += high[length-i-1]

        #Increment count by three
        count += 3
        
    return print(converted)

#Test case: 1
num1 = 123
integerToEnglishCurrency(num1)

#Test case: 2
num2 = 12345
integerToEnglishCurrency(num2)

#Test case: 3
num3 = 1234567
integerToEnglishCurrency(num3)

