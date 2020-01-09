# Import Counter
import re
from nltk import word_tokenize
from collections import Counter

with open('design-portfolio.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')

# Tokenize the article: tokens
tokens = word_tokenize(data)

# Convert the tokens into lowercase: lower_tokens
lower_tokens = [t.lower() for t in tokens]


# Create a Counter with the lowercase tokens: bow_simple
bow_simple = Counter(lower_tokens)



# Print the 10 most common tokens
print(bow_simple.most_common(2))
