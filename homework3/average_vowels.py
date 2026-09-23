# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

def counting_vowels_and_consonants(p):
    x = len(p)
    y = p.lower()
    v = 0
    c = 0
    for i in range(x):
        if y[i] in "aeiou":
            v = v + 1
        else:
            c = c + 1
    a = str(v)
    b = str(c)
    return(a, b)
    #print("This string has " + a + "vowels and " + b + "constonants.")
#print(counting_vowels_and_contonants("emma"))
        
# Hint: You can use .isalpha() to check if a character is a letter.

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()
def average_vowels_and_consonants(p):
    s = 0
    x = len(p)
    for i in range(x):
        if p[i] == "!" or p[i] == "." or p[i] == "?":
            s += 1
    stoiv = int(counting_vowels_and_consonants(p)[0])
    stoic = int(counting_vowels_and_consonants(p)[1])
    ava = stoiv / s
    avc = stoic / s
    return(s, ava, avc)



# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

print(f"The average vowels per sentence for the paragraph is {average_vowels_and_consonants(paragraph)[1]} and the average consonants per paragraph is {average_vowels_and_consonants(paragraph)[2]}")
