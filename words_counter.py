from itertools import groupby
file_path = "C:\\Users\\noor1\\Desktop\\notmyfile.txt"
counters = {} # Initialize counting dictionary
with open(file_path, 'r') as f: 
    content = f.read() 
    words = content.split()
for word in words:
    word = word.upper() # Make the word all caps
    if word not in counters:
            counters[word] = 1 # First occurrence, add the counter
    else:
        counters[word] += 1 # Increment existing counter
    # Report the counts for each word
for word, count in counters.items():
    print(word,count)
words.sort(key=len)
output = [list(set(items)) for length, items in groupby(words, key=len)]
print(output)