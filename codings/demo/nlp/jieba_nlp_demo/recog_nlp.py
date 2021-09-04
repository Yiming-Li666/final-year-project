#encoding=utf-8
from __future__ import unicode_literals

import sys
sys.path.append("../")

import jieba
jieba.load_userdict("./dic.txt")
import jieba.posseg
import jieba.analyse
import difflib
import Levenshtein
from fuzzywuzzy import fuzz

str1 = '2020年1月1日，病人编号000003宝宝37周一直成奶粉喂养，每天六次，每次140毫升左右，之前每天天一次大便从四个月开始一直持续废死，益生菌上周六开始，突然一天大便两次有奶瓣了个粘液。周日拿了五次，周一白天正常，可是晚上到了今天差不多一天五次左右一次喂奶没一会儿就放屁，大便每次不是很多，这两天五米，他的农浓度稀释了，基本上120毫升容易水才给一勺奶粉喂奶，瓶子增加还是拉米饭，可能是乳糖不耐受可以吃蒙脱粉和复方胃蛋白酶奶粉暂时停止。'
str2 = '2020年1月1日，病人编号00003。宝宝37周+1出生，一直纯奶粉喂养，每天6次，每次140ml左右，之前每天一次大便。从4个月开始一直吃lifespace益生菌。上周六开始突然一天大便两次，有奶瓣和粘液，周日拉了5次。周一白天正常，可是晚上开始到今天差不多一天5次左右，一喂奶没一会就放屁大便。每次不是很多，这两天我们自己给她吧奶浓度稀释了，基本上120ml的水才给1勺奶粉，喂奶频次增加。但还是拉奶瓣。可能是乳糖不耐受，可以吃蒙脱粉和复方胃蛋白酶，奶粉暂时停吃。'

test1 = difflib.SequenceMatcher(None, str1, str2).quick_ratio()
test2 = Levenshtein.ratio(str1, str2)
test3 = fuzz.ratio(str1, str2)

print(test1)
print(test2)
print(test3)


print('3. 关键词提取')
print('-'*40)
print(' TF-IDF')
print('-'*40)

# s = "2020年1月1日，病人编号00001。小孩出生12天有咳嗽，拍片说是肺炎，医院要求住新生儿科打抗生素，住院一周出院继续有咳嗽，医生让服用进口阿奇霉素，服用2天患者晚上哭闹不睡，肚子拉稀。还是继续咳嗽，每天5声左右。在住院期间患者吃了进口阿奇霉素5天 然后停了几天 出院宝宝还咳嗽 又让继续喂5天 现在已经喂3天了。医院让重新拍了个片对比，比第一次阴影稍微吸收了一点。然后说如果咳嗽就让再次住院。有口服的阿莫西林克拉维酸钾，商品名是铿锵或者棒林，可以买来继续给孩子使用3天左右。同时可给孩子吃些止咳化痰的中成药，例如：小儿咳嗽糖浆、小儿止咳糖浆等等。如果5天后情况仍无好转，建议去复诊，或者去更上级的医院复诊。"
for x, w in jieba.analyse.extract_tags(str1, withWeight=True):
    print('%s %s' % (x, w))
print('='*40)
for x, w in jieba.analyse.extract_tags(str2, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)

for x, w in jieba.analyse.textrank(str1, withWeight=True):
    print('%s %s' % (x, w))

print('='*40)
for x, w in jieba.analyse.textrank(str2, withWeight=True):
    print('%s %s' % (x, w))

# print('='*40)
# print('4. 词性标注')
# print('-'*40)


# jieba.enable_paddle()
# jieba.suggest_freq(('个','片'), True)
# words = jieba.posseg.cut(s,HMM=False)
# for word, flag in words:
#     print('%s %s' % (word, flag))
# words = jieba.posseg.cut(s,use_paddle=True)
# for word, flag in words:
#     print('%s %s' % (word, flag))