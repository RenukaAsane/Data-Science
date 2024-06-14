# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:24:04 2024

@author: Admin
"""

##################################################
'''Python for NLP'''
############Test Mining########################

sentence="we are learning TextMining from Sanjivani AI"
###if we want to know position of learning
sentence.index("learning")
#It will show learning is at position 7
#This is going to show character position from 0 including

#################################

#we want to know position TextMining word
sentence.split().index("TextMining")
sentence.split().index("learning")
#it will split the words in list and count the position
#if u want to see the list select sentence.split() and 
#it will show at 3

#########################################
#suppose we want to print any word in reverse order
sentence.split()[2][::-1]
#[start:end end:-1(start)] will start from -1,-2,-3 till
#learning will be printed as gninrael

#######################################################

words=sentence.split()
first_word=words[0] #this is going to do tokenization
first_word
last_word=words[-1]
last_word


###now we want ot concat the 1st and last word
concat_word=first_word+" "+last_word
concat_word

############################################################3
#we want to print even words from the sentences
[words[i] for i in range(len(words)) if i%2==0]
#words having odd length will not be printed

####################################################
sentence
#now we want to display only AI
sentence[-3:]
#it will start from -3,-2,-1 that 8s space ,A and I
###############################33
#suppose we want to display entire sentence in reverse order
sentence[::-1]
#'IA inavijnaS morf gniniMtxeT gninrael era ew'

##################################################3
#suppose we want to select each word and print in reversed word
words
print( " ".join(word[::-1]for word in words))
## o/p :- ew era gninrael gniniMtxeT morf inavijn=baS IA

########################################################

'''tokenization'''
#
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)

###################################
#Parts of Speech (PoS) tagging
nltk.download("averaged_perceptron_tagger")
nltk.pos_tag(words)
#It will mention parts of speech

###################################

#stop word from NLTK library
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words=stopwords.words("English")
#u can verify 179 stop words in variable explorer
print(stop_words)

###############################################
#suppose we want to replace words in string
sentence2="I visited MY from IND on 14-02-19"
normalized_sentence=sentence2.replace("MY","Malaysia").replace("IND","India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

####################################################
#suppose we want auto correction in the sentence
from autocorrect import Speller
#declare the function Speller from English
spell=Speller(lang="en")
spell("Engnier")

##################################################
import nltk
nltk.download("punkt")
from nltk import word_tokenize
sentence3="Ntural language processin deals withh the aart of extractin sentimentts"
#us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)

###############################################3
#Stemming 
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")

########################################################33
#Lematizer
#lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("ammazing")

##################################################33
###Chunking (Shallow Parsing)Identifying named entities
nltk.download("maxent_ne_chunker")
nltk.download("words")
sentence4="We are learning NLP in python by SanjivaniAI"
#first we will tokenize
nltk.download("averaged_perceptron_tagger")
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

#############################################3
#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python. Deliverd by Sanjivani")
sent
#o/p :-  ['we are learning NLP in python.', 'Deliverd by Sanjivani']

########################################################
#He went to bank and checked account it was almost 0
#looking this he went to river bank and was crying
from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1), 'bank'))
###o/p :- Synset('savings_bank.n.02')

sentence2="It is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2), "bank"))
#o/p : - Synset('bank.v.07')

##################################################
'''Removing Special Characters'''
'''
Special characters are non-alpha numerical
characters.These characters are most often found in 
comments,references,currency numbers etc. 
These characters add no value to text 
understanding and induse noice into algorithms.
For that regex package is used.'''
'''regex101.com'''

import re

chat1="Hello, I am having an issue with my order # 376335786"

pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches

#######################################################
chat2="I have a problem with my order 376335786"
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches

#######################################################
chat3='My order 376335786 is having an issue, I was charged'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches

#####################################################
def get_pattern_match(pattern,text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(/d*)',chat1)   
    
    
    
    
    