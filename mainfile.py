import spacy

def bigram(doc):
    # create a list for the result
    result = list()
    # create a list that contains no punctuation
    sentence = list()
    # parse through the document to add all tokens that are words to the sentence list
    for token in doc:
        if token.is_alpha:
            sentence.append(token)
    # parse through the sentence while adding words in groups of two to the result
    for word in range(len(sentence) - 1):
        first_word = sentence[word]
        second_word = sentence[word + 1]
        element = [first_word.text, second_word.text]
        result.append(element)

    return result

def main():
    # load English model
    nlp = spacy.load('ur')

    # create a document
    doc = nlp("غم ہستی کا اسدؔ کس سے ہو جز مرگ علاج")

    result = bigram(doc)

    for element in result:
        for token in element:
            print(token, end=' ')
        print()  # new line


main()