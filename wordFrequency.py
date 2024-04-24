import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Read the contents of the "random_paragraphs.txt" file
with open('random_paragraphs.txt', 'r') as file:
    text = file.read()

# Tokenize the text
words = nltk.word_tokenize(text)

# Remove stop words using NLTK library
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]

# Count the frequency of each word in the processed text
word_freq = Counter(filtered_words)

# Display the word frequency count to the console
for word, freq in word_freq.most_common(): #=>in descending order ,in word_freq.items()=>not in descending order
    print(f'{word}: {freq}')
