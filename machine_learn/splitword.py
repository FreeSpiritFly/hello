# -*- coding: UTF-8 -*-
import sys
import os
import jieba
reload(sys)
sys.setdefaultencoding('utf-8')
seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=False)
print "Default Mode:"," ".join(seg_list)
seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=False)
print "No Mode:"," ".join(seg_list)
seg_list = jieba.cut("小明1995年毕业于清华大学", cut_all=True)
print "Full Mode:"," ".join(seg_list)
seg_list = jieba.cut_for_search("小明硕士1995年毕业于中国科学院计算所，后在日本京都大学深造")
print "Default Mode:"," ".join(seg_list)
def savefile(savepath,content):
    fp = open(savepath,"wb")
    fp.write(content)
    fp.close()
def readfile(path):
    fp = open(path,"rb")
    content = fp.read()
    fp.close();
    return content

corpus_path = "./corpus/"
seg_path = "./seg/"
catelist = os.listdir(corpus_path);

for mydir in catelist:
    class_path = seg_path + mydir +"/"
    if not os.path.exists(seg_dir):
        os.makedirs(seg_dir)
    file_list = os.listdir(class_path)
    for file_list in file_list:
        fullname = class_path + file_path
        content = readfile(fullname).strip()
        content = content.replace("\r\n","").strip()
        content_seg = jieba.cut(content)
        savefile(seg_dir+file_path," ".join(content_seg))
print  "分词结束"
