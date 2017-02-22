# -*- coding: utf-8 -*-
from collections import Counter
#import re #看别人用的正则表达来处理文本，但自己用的不好，待学习。

#with open('happiness_seg.txt','r') as wordsfile:
#    for words in wordsfile:
#        word = words.split(' ')
'''为什么我用上面的代码做出的词典只有最后一段？没想明白。'''

wordsfile = open("happiness_seg.txt")
content = wordsfile.read()
word = content.split(" ")
'''将文本拆成词典'''

bp_dic = []
'''建立一个列表装二元词组'''
punctuation = [',','。',':','、','（','）','--','“','”','？','；','，','―']
'''建立一个词典装文中出现的标点，供后面用'''
while len(word) > 1:
    '''循环语句，当列表元素数大于1就执行'''
    if word[0] in punctuation:
        '''如果第一项是标点，那么就删除第一项'''
        del word[0]
    elif word[1] in punctuation:
        '''如果第二个元素是标点，那么就删除第一和第二项'''
        del word[0],word[1]
    else :
        '''如果前两项都不是标点，那么组合成二元词组,再把第一项删除，继续循环。'''
        binary_phrase = word[0] + word[1]
        bp_dic.append(binary_phrase)
        del word[0]

word_counts = Counter(bp_dic)
top_10 = word_counts.most_common(10)
'''计数并输出前十最多的'''

print (top_10)

#[('的人', 918), ('自己的', 474), ('他的', 401), ('上的', 355), ('人的', 282), ('他们的', 271), ('的时候', 261), ('的东西', 206), ('的生活', 191), ('的孩子', 190)]
