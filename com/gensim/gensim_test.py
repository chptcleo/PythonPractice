import gensim
import os

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
                
# sentences = word2vec.Text8Corpus('./gensim_file1')
# model = word2vec.Word2Vec(sentences)
sentences = MySentences('./') # a memory-friendly iterator
model = gensim.models.Word2Vec(sentences)
model.save('./model1')
model.wv.most_similar(positive=['woman', 'king'], negative=['man'])
