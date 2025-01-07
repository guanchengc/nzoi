import re, string
text = input()
text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
text = re.sub(r'[0-9]+', '', text)
words = set(text.lower().split())
words.sort()
for word in words:
    print(word)
