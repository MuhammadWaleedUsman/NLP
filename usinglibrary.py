# Here are the libraries used
import numpy as np
import spacy

nlp = spacy.blank('ur')

# The files which are to be used
file_path_iqbal = 'data/iqbal.txt'
file_path_faiz = 'data/faiz.txt'
file_path_ghalib = 'data/ghalib.txt'
lines = []
words = []

# Converting to word set
text_file_iqbal = open(file_path_iqbal, mode='r', encoding='utf-8-sig')
text_file_faiz = open(file_path_faiz, mode='r', encoding='utf-8-sig')
text_file_ghalib = open(file_path_ghalib, mode='r', encoding='utf-8-sig')
text_file_read = text_file_iqbal.readlines() + text_file_faiz.readlines() + text_file_ghalib.readlines()
#print(text_file_read)
for line in text_file_read:
    line_clean = line.rstrip('\n')
    lines.append(nlp(line_clean))

print("Urdu Tokenization using SpaCy")
for line in lines:
    for word in line:
        words.append(str(word))

for word in words:
    if word == '،':
        words.remove(word)
    elif word == '%':
        words.remove(word)
    elif word == '‘':
        words.remove(word)
    elif word == '؟':
        words.remove(word)
    elif word == '"':
        words.remove(word)
    elif word == '!':
        words.remove(word)


while '٪' in words:
    words.remove('٪')

uni_gram = words
bigram = []
print(uni_gram)

for word in uni_gram:



