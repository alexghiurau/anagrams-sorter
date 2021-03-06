import sys
# -----------------------------------------------------------
# Takes words from a file and groups all anagrams, writing 
# back to a designated file.
#
# By Alex Ghiurau
# -----------------------------------------------------------

def sortAnagrams(lines):
    # create a dictionary, key is the sorted word, value is a 
    # list of words (including any anagrams)
    dictionary = {}

    for line in lines:
        # sort each word's characters alphabetically
        sortedLine = ''.join(sorted(line))
        if sortedLine in dictionary:
            # if in dict, append next to other anagram
            dictionary[sortedLine].append(line)
        else:
            dictionary[sortedLine] = [line]

    # use dictionary to map out an array of words, for writing to file
    anagrams = [dictionary[k] for k in dictionary]

    writeToFile(anagrams)

# read from user-specified file passed as parameter
def readFromFile():
    
    with open(sys.argv[1], 'r') as reader:
        # create array with each word from file
        words = [word.strip() for word in reader]

        # remove duplicate words
        words = set(words)
        
        sortAnagrams(words)

# write to the file 'sortedWords.txt', replacing existing data (if any)
def writeToFile(anagrams):
    with open('sortedWords.txt', 'w') as writer:
        for anagram in anagrams:
            writer.write(' '.join([str(s) for s in list(anagram)]) + '\n')
    print("Task has been completed.")

# main function that initialises the process
def main():
    readFromFile()

# when program loads, start main function
main()