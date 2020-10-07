# Here are the libraries used
import numpy as np
import spacy
import pandas as pd
from itertools import chain
import random
nlp = spacy.blank('ur')


def n_grams(seq, n):
    shift_token = lambda i: (el for j, el in enumerate(seq) if j >= i)
    shifted_tokens = (shift_token(i) for i in range(n))
    tuple_ngrams = zip(*shifted_tokens)
    return tuple_ngrams


def range_ngrams(list_tokens, n):
    ngram_range = (n, n + 1)
    return chain(*(n_grams(list_tokens, i) for i in range(*ngram_range)))


if __name__ == '__main__':
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

    # Tokenizing
    for line in text_file_read:
        line_clean = line.rstrip('\n')
        lines.append(nlp(line_clean))

    # Separating the words from the lines
    for line in lines:
        for word in line:
            words.append(str(word))

    # Removing unwanted strings
    uni_gram = list(filter(None, (map(lambda x: x.replace('،', '').replace('%', '').replace('!', '').replace('%', '').
                                      replace('(', '').replace(')', '').replace(':', '').replace('.', '').replace(' ',
                                                                                                                  '').
                                      replace("'", '').replace('"', '').replace('“', '').replace('۔', '').replace('‘',
                                                                                                                  '').
                                      replace('’', '').replace('؟', '').replace('٪', ''), words))))
    print(uni_gram)
    # Bi gram model
    bi_gram_model = list(range_ngrams(uni_gram, 2))
    print(bi_gram_model)
    bi_gram_model = [' '.join(words) for words in bi_gram_model]
    print(bi_gram_model)

    # Tri gram model
    tri_gram_model = list(range_ngrams(uni_gram, 3))
    tri_gram_model = [' '.join(words) for words in tri_gram_model]
    print(tri_gram_model)

    # Frequencies of the words repeated
    uni_gram_df = pd.DataFrame(uni_gram, columns=['unigram'], dtype=str)
    uni_gram_df_freq = uni_gram_df.groupby('unigram').size().reset_index(name='unigram_frequency')
    uni_model_sort = uni_gram_df_freq.sort_values(by='unigram_frequency', ascending=[0])
    uni_model_sort.to_csv('unigram.csv', index=False, header=True)

    bi_gram_df = pd.DataFrame(bi_gram_model, columns=['bigram'], dtype=str)
    bi_gram_df_freq = bi_gram_df.groupby('bigram').size().reset_index(name='bigram_frequency')
    bigram_model_sort = bi_gram_df_freq.sort_values(by='bigram_frequency',ascending=[0])
    bigram_model_sort.to_csv('bigram.csv', index=False, header=True)

    tri_gram_df = pd.DataFrame(tri_gram_model, columns=['trigram'], dtype=str)
    tri_gram_df_freq = tri_gram_df.groupby('trigram').size().reset_index(name='trigram_frequency')
    trigram_model_sort = tri_gram_df_freq.sort_values(by='trigram_frequency', ascending=[0])
    trigram_model_sort.to_csv('trigram.csv', index=False, header=True)

    random_top_50 = uni_gram_df_freq.nlargest(50, ['unigram_frequency'])['unigram'].to_list()
    bigram_model_list_sorted = bigram_model_sort['bigram'].to_list()
    tri_model_list_sorted = trigram_model_sort['trigram'].to_list()
    #print(bigram_model_list_sorted)
    pick_random_1 = random.choice(random_top_50)
    print('\n\n')
    print('Random_number')
    print(pick_random_1)
    print('\n')
    print('Bigram Predictions')
    counter = 0
    # Prediction for Bigram model
    for word in bigram_model_list_sorted:
        first_word = word.split(' ')[0]
        if pick_random_1 == first_word:
            second_word = word.split(' ')[1]
            print("Forward Prediction")
            print(first_word + ' ' + second_word)
            print("Backward Prediction")
            print(second_word + ' ' +  first_word)
            counter += 1

        if counter == 3:
            break
    print('\n\n')
    print('Trigram Predictions')
    counter = 0
    # Prediction for Bigram model
    for word in tri_model_list_sorted:
        first_word = word.split(' ')[0]
        if pick_random_1 == first_word:
            second_word = word.split(' ')[1]
            third_word = word.split(' ')[2]
            print("Forward Prediction")
            print(first_word + ' ' + second_word + ' ' + third_word)
            print("Backward Prediction")
            print(third_word + ' ' + second_word + ' ' + first_word)
            counter += 1

        if counter == 3:
            break


