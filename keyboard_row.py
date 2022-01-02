# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# Author: KharelUtsav


data = ["asdfghjkl", "qwertyuiop", "zxcvbnm"]
words = ["Hello","Alaska","Dad","Peace"]

def function(word):
    for i in range(3):
        count = 0
        for letter in word.lower():
            if letter in data[i]:
                count += 1
            else:
                i += 1
                break
        if len(word) == count:
            return word

def keyboard_row(words):
    matched_words = [word for word in words if word == function(word)]
    return matched_words

print(keyboard_row(words))

