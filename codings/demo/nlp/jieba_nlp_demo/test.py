#encoding=utf-8
from __future__ import unicode_literals

import sys
sys.path.append("../")

import jieba
jieba.load_userdict("./dic.txt")
import jieba.posseg
import jieba.analyse

print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

s = "2020年1月1日，病人编号00001。小孩出生12天有咳嗽，拍片说是肺炎，医院要求住新生儿科打抗生素，住院一周出院继续有咳嗽，医生让服用进口阿奇霉素，服用2天患者晚上哭闹不睡，肚子拉稀。还是继续咳嗽，每天5声左右。在住院期间患者吃了进口阿奇霉素5天 然后停了几天 出院宝宝还咳嗽 又让继续喂5天 现在已经喂3天了。医院让重新拍了个片对比，比第一次阴影稍微吸收了一点。然后说如果咳嗽就让再次住院。有口服的阿莫西林克拉维酸钾，商品名是铿锵或者棒林，可以买来继续给孩子使用3天左右。同时可给孩子吃些止咳化痰的中成药，例如：小儿咳嗽糖浆、小儿止咳糖浆等等。如果5天后情况仍无好转，建议去复诊，或者去更上级的医院复诊。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(s, withWeight=True):
    print('%s %s' % (x, w))

print('='*40)
print('4. 词性标注')
print('-'*40)


jieba.enable_paddle()
jieba.suggest_freq(('个','片'), True)
words = jieba.posseg.cut(s,HMM=False)
for word, flag in words:
    print('%s %s' % (word, flag))
words = jieba.posseg.cut(s,use_paddle=True)
for word, flag in words:
    print('%s %s' % (word, flag))