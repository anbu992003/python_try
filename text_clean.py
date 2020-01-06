
b
from textblob import TextBlob
 
#data = "Natural language is a cantral part of our day to day life, and it's so antresting to work on any problem related to langages."

data = "the borrowe is not in agriment"
 
output = TextBlob(data).correct()
print(output)



#2- Levenshtein distance
def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    lensum = float(m + n)
    d = []           
    for i in range(m+1):
        d.append([i])        
    del d[0][0]    
    for j in range(n+1):
        d[0].append(j)       
    for j in range(1,n+1):
        for i in range(1,m+1):
            if str1[i-1] == str2[j-1]:
                d[i].insert(j,d[i-1][j-1])           
            else:
                minimum = min(d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1]+2)         
                d[i].insert(j, minimum)
    ldist = d[-1][-1]
    ratio = (lensum - ldist)/lensum
    return {'distance':ldist, 'ratio':ratio}
 
print(levenshteinDistance("kitten","sitting"))   
print(levenshteinDistance("rosettacode","raisethysword"))


#https://haptik.ai/tech/extract-spelling-mistakes-fasttext/
#3 -  Fastext
import io
import collections
#import matplotlib.pyplot as plt
#import nltk
#import enchant


words = []
with io.open('/Users/anbu/kaggle/demofile3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        words.extend(line.split())

vocab = collections.Counter(words)
print(vocab.most_common(10))

list(reversed(vocab.most_common()[-10:]))



