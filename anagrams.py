import sys
# -----------------------------------------------------------
# Takes words from a file and groups all anagrams, writing 
# back to a designated file.
#
# By Alex Ghiurau
# -----------------------------------------------------------

"""groupAnagrams - Function to group anagrams from a given list of words
   Args:
        words (array): array of words taken from user provided file
   Returns:
        anagrams (array): an array words where anagrams are grouped"""
def groupAnagrams(words):
    # a list to store anagrams
    anagrams = []
 
    # return if no words are found
    if not words:
        return anagrams
 
    # sort the characters of each word in alphabetical order
    sortedChars = [''.join(sorted(word)) for word in words]
 
    # create a dictionary where the key is each sorted chars instance,
    # and the value is a list of indices where they are found
    dictionary = {}
    for index, sortedWord in enumerate(sortedChars):
        dictionary.setdefault(sortedWord, []).append(index)
 
    # use the dictionary to map out the array, grouping anagrams
    # using using tuples and the indices from the dictionary.
    for index in dictionary.values():
        collection = tuple(words[i] for i in index)
        anagrams.append(collection)
    
    return anagrams

# create array to store the words from the provided file, which is then 
# passed to groupAnagrams()
wordsFromFile = []

# using 'with open' to ensure the file is opened/closed correctly
# this method ensures we do not open the whole file at once, but line by line
# which is important considering the limited memory assumption
# file name is passed as args
with open(sys.argv[1], 'r') as reader:
    for line in reader:
        wordsFromFile.append(line.rstrip())
 
anagrams = groupAnagrams(wordsFromFile)

# similar to above but we write in a separate file in case the original must stay intact
# if this file does not exist, it gets created otherwise all text is replaced by new output
with open('sortedWords.txt', 'w') as writer:
    for anagram in anagrams:
        writer.write(' '.join([str(s) for s in list(anagram)]) + '\n')