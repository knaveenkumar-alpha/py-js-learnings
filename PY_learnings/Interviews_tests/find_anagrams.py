st = """John is at a post, where they make pots. Making the pots will
stop in the future. Oh dear, what will happen to them when it 
happens. This can happen only in Rome, Read on to find more."""

# split the text into words, remove punctuation, and convert to lowercase.add()
words = [word.lower().strip('.,"') for line in st.split('\n') for word in line.split()]
print(words)
#create a dictionary to group anagrams
anagrams = {}
for word in words:
    # sort the words to create a key for anagrams
    key = ''.join(sorted(word))
    if key in anagrams:
        anagrams[key].append(word)
    else:
        anagrams[key] = [word]
# Filter out lists with more than one anagram
print("===========================================================================")
print(anagrams)
res = {tuple(group) for group in anagrams.values() if len(group) > 1 and group[0] != group[1]}


print(res)
