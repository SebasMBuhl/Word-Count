
# Online Python - IDE, Editor, Compiler, Interpreter
import string

def count(word, sentence):
    
    sentence = sentence.lower()
    word = word.lower()
    
    translator = str.maketrans("", "", string.punctuation)
    sentence = sentence.translate(translator)
    
    num = sentence.split().count(word)
    
    print("The word", word, "appears", num, "times")

word = input("What word are you searching? ")
sentence = input("What sentence should this word be searched in? ")

count(word, sentence)
word = input("What word are you searching?")
sentence = input("What sentence should this word be searched in?")

count(word,sentence)


