word = input("Enter any word or any sentence :- ")

vowels = 0
consonants = 0

for ch in word:

    if ch.isalpha():

        if ch.lower() in "aeiou":
            vowels +=1
        
        else:
            consonants +=1
    
total_letters = vowels + consonants

print(f"Total Letters = {total_letters}")
print(f"Total vowels in {word} = {vowels}")
print(f"Total consonanta in {word} = {consonants}")