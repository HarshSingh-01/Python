# Pig_latin
# apple:- appleay ("vowel")
# word:- ordway ("consonant")

def pig_latin(word):
    first_letter = word[0]       # picking the first word 
    if first_letter in "aeiou":  # condition for checking the first word is vowel or not
        print (word + 'ay')
    else:
        print (word[1:] + first_letter + 'ay')

word = input('Input your word: ') # User input
pig_latin(word)

