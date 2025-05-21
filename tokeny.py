import nltk
nltk.download('punkt')

sentence = "Tokenisation is the process of splitting a sentence into words."
tokens = nltk.word_tokenize(sentence)
print(tokens)
