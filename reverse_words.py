# reverse_strings.py
# by Kevin dela Cruz for Persol Group

input_string = "My name is kevin"
splitter = " "

#tokenize strings
words = input_string.split(splitter)
words.reverse()

rev_words = ""

for word in words:
    rev_words += word
    rev_words += " "

print(rev_words[:-1])
