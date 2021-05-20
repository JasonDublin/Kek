import requests
import collections
import pandas as pd
import matplotlib.pyplot as plt

file_name = input("What file would you like to open? ")
with open(file_name, "r") as f:
    words = f.read().split()

search_words = input("What words do you want to find? ").split(',')
search_words = [word.strip().lower() for word in search_words]
#print(search_words)
search_counts = dict.fromkeys(search_words, 0)

print ('\n... analyzing ... hold on ...')
for word in words:
    word = word.rstrip(",.").lower()
    if word in search_counts:
        search_counts[word] += 1

print ('\nFrequency of word usage within', file_name + ":")
for word in search_words:
    print("   {:<20s} / {} occurrences".format(word, search_counts[word]))
#ikaw gumawa ng mag input ng tt file naka manual set kasi hehe thanks
file = open('kek.txt', encoding="utf8" )

a= file.read()

# Stopwords para lang di masama mga usual words like mr ms mga ganun pwede naman yan tangalin
stopwords = set(line.strip() for line in open('kek.txt'))
stopwords = stopwords.union(set(['mr','mrs','one','two','said']))
# stopwords na txt file para lang ma exclude sa bibilangin na words,
# Add to the dictionary if it doesn't exist. If it does, increase the count.
wordcount = {}
# para lang ma eliminate ung mga duplicates
for word in a.lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace(":","")
    word = word.replace("\"","")
    word = word.replace("!","")
    word = word.replace("â€œ","")
    word = word.replace("â€˜","")
    word = word.replace("*","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(wordcount)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)
# Close the file
file.close()
# Create a data frame of the most common words
# Draw a bar chart
lst = word_counter.most_common(n_print)
df = pd.DataFrame(lst, columns = ['Word', 'Count'])
df.plot.bar(x='Word',y='Count')

plt.xlabel('words', fontsize = 12)
plt.ylabel('count', fontsize = 12)

#para sa range
plt.xlim(0,10)
plt.ylim(0,20)

#para sa title
plt.title('Words frequency', fontsize = 20)
plt.legend()
plt.show()