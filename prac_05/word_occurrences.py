"""
Word Occurrences
Estimate: 15 minutes
Actual: 30 minutes
"""

from operator import itemgetter

word_to_count = {}
text = input("Text: ").split(' ')
for word in text:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1
sorted(word_to_count.items(), key=itemgetter(0))
longest_word_length = max(len(word) for word in word_to_count)
for word, number_of_appearances in word_to_count.items():
    print(f"{word:{longest_word_length}} : {number_of_appearances}")
