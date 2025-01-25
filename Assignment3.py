#1. Input sentence details
sentence = input("Enter a sentence: ")

#2. Output senence details
print("The sentence is",len(sentence),"characters long")
word_order = sentence.split(" ")
print('First word is: ' + word_order[0] + "\nLast word is: " + word_order[-1]) 

#3. Indexing and Slicing
print('The first three characters are:', sentence[0:3])
print('The last three characters are:', sentence[-3:])
print(sentence[::-1])

#4. Modify the sentence
print(sentence.upper())
print(sentence.lower())
print(sentence.replace(" ", "-"))