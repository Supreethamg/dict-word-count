def wordcount(filename):
    ''' Reads text input file and counts how many times
     each space-separated word occurs in that file.
      Prints those counts to the screen.'''
    word_count = {}
    file_data = open(filename)
    for line in file_data:
        words = line.split()
        for word in words:
            word_count[word.rstrip()] = word_count.get(word.rstrip(),0) +1
    print(word_count)
    return word_count


word_dict = wordcount("twain.txt")
for  word ,count in word_dict.items():
    print (f'{word} {count}')