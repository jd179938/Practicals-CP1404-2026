"""
Word Occurrences
Estimate: 15 minutes
Actual: minutes
"""

word_to_count = {}
text = input("Text: ").split(' ')
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

print(word_to_count)
