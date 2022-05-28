# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from asyncore import read


def read_file_content(filename):
    with open(filename) as file_object:
        open_file= file_object.read()
    
    return open_file


def count_words():
    text = read_file_content(".\story.txt")
    counts=dict()
    words = text.split()
    for i in words:
        if i in counts:
            counts[i] +=1
        else:
            counts[i]=1
    
    return counts
    






   
    
        

    