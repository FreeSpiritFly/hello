# -*- coding: utf-8 -*-
import sys
import os
from sklearn.datasets.base import Bunch
import cPickle as pickle
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

reload(sys)
sys.setdefaultencoding('utf-8')

def readbunchobj(path):
    file_obj = open(path,"rd")
    bunch = pickle.load(file_obj)
    file_obj.close()
    return bunch

def writebunchobj(path,bunchobj):
    file_obj = open(path,"wb")
    pickle.dump(bunchobj,file_obj)
    file_obj.close()

path = "train_word_bag/train_set.dat"
bunch = readbunchobj(path)

tfidfspace  = Banch(target_name = bunch.target_name,labal = banch.label,filenames = bunch.filenames,tdm=[],vocabulary={})
vectorizer = TfidfVectorizer(stop_words=stpwrdlist,sublinear_tf = True,max_df = 0.5)
transformer=TfidfTransformat()
tfidfspace.tdm = vectorizer.fit_transform(bunch.contents)
tfidfspace.vocabulary = vectorizer.vocabulary_
space_path = "train_word_bag/tfdifspace.dat"
writebunchobj(space_path,tfidfspace)

