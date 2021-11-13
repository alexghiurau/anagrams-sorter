# anagrams-sorter - Instructions

## Launching the application

1. Make sure to use the correct path to the words file. Usually the easiest to put the file in the same directory as anagrams.py

2. Into the terminal, type

```
python anagrams.py filename.txt
```

3. Currently there is no indication of the progress, but once complete the new file "sortedWords.txt" should be created and have all the anagrams grouped as needed. Lone words will still be displayed. Note the sortedWords.txt file is created in the same directory as anagrams.py

## Example use case

```
python anagrams.py words.txt
```

### Input

```
apple
car
cider
tar
itch
rat
cried
helicopter
arc
```

### Output

```
apple
car arc
cider cried
tar rat
itch
helicopter
```

I also included a ~5MB file called wordsBig.txt which contains a lot more words to test this application, about 500K lines.
