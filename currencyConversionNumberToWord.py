
# Online Python - IDE, Editor, Compiler, Interpreter
#1234
num = 1234567000
# if num == 0:
#     return 'Zero';

numStr = str(num)
if 3-(len(numStr) % 3) != 3:  
    numStr = ((3-(len(numStr) % 3)) * '0') + numStr
    
high = ['', 'Thousand ', 'Million ', 'Billion ', 'Trillion ']
Tens = ['', 'Ten ', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
Teens = ['', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ', 'Nineteen ']
BelowTen = ['', 'One ', 'Two ', 'Three ', 'Four ', 'Five ', 'Six ', 'Seven ', 'Eight ', 'Nine ']
length = len(numStr) // 3
converted = ""
count = 0
for i in range(length):
    one = int(numStr[count + 0])
    two = int(numStr[count + 1])
    three = int(numStr[count + 2])
    
    #hundred
    converted += BelowTen[one]
    if one > 0:
        converted += 'Hundred '
    
    #tens
    if two == 0:
        converted += BelowTen[three]
        
    elif three == 0:
        converted += Tens[two]
        
    elif two == 1:
        converted += Teens[three]
    
    else:
        converted += Tens[two] + BelowTen[three]
        
    converted += high[length-i-1]
    count += 3
print(converted)
        
        

