import os, gensim
from itertools import islice
from gensim.parsing.preprocessing import preprocess_string


def iter_documents(top_directory):
    """Iterate over all documents, yielding a document (=list of utf8 tokens) at a time."""
    for root, dirs, files in os.walk(top_directory):
        for file in filter(lambda file: file.endswith('.TXT'), files):
#            document = open(os.path.join(root, file)).read() # read the entire document, as one big string
#            print(document)
            #Read first 50 lines from file
            with open(os.path.join(root, file)) as myfile:
                head = list(islice(myfile, 50))
#            print(head)                
            document = ' '.join(preprocess_string(' '.join(head).replace('\n', ' ').replace('\r', '')))
            print(document)
            f = open("demofile3.txt", "a")
            f.write( "test\t" + document + "\n")
            f.close()
            yield gensim.utils.tokenize(document, lower=True) # or whatever tokenization suits you

class MyCorpus(object):
    def __init__(self, top_dir):
        self.top_dir = top_dir
        self.dictionary = gensim.corpora.Dictionary(iter_documents(top_dir))
        self.dictionary.filter_extremes(no_below=1, no_above=0.5, keep_n=1000) # check API docs for pruning params

    def __iter__(self):
        for tokens in iter_documents(self.top_dir):
            yield self.dictionary.doc2bow(tokens)

corpus = MyCorpus('/Users/anbu/Downloads/windows_aspi_10701/') # create a dictionary
for vector in corpus: # convert each document to a bag-of-word vector
    print (vector)
