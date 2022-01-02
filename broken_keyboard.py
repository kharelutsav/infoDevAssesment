# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Author: KharelUtsav


def broken_keyboard(text, broken_letters): #Arguments type: String, String; Return Type: Number/Integer
    """
    broken_keyboard function takes in text and broken_letters as arguments. Text is string of words
    separated by spaces. broken_letters is string which contains characters that can not be typed
    by the keyboard.
    This function evaluates the words that contain the broken letters and returns the maximum length 
    of the words that can be succesfully typed.
    """

    #text => list(text)
    words = text.split(" ")

    #Count variable to store broken words
    count = 0
    #Loop through the words list
    for word in words:
        #Loop through the broken_letters String to gain individual characters
        for letter in broken_letters:
            #Checks if the letter is present in word
            if letter in word:
                #Increment count by one
                count += 1
                #Break the loop
                break
    print(len(words) - count) #words.length - count
        
    
    
#Test case: 1
text_1 = "hello world"
brokenLetters_1 = "ad"   
broken_keyboard(text_1, brokenLetters_1)

#Test case: 2
text_2 = "hello world one"
brokenLetters_2 = "af"   
broken_keyboard(text_2, brokenLetters_2)

