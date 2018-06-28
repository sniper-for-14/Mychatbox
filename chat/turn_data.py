# -*- coding=utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
import jieba
import numpy as np
import re

posts = [open('chat/ask_answer.csv').read()]
vectorizer = CountVectorizer(min_df=1)

X_train = vectorizer.fit_transform(posts)

# print(X_train.toarray().shape)

content = posts[0].split('\n')


# np_array = np.ndarray([1041,1155])
# files = csv.reader(open('ask_answer.csv','r'))
# So_Many_Fish = []
# count_j = 0
# for i in files:
#     new_post = i[0]
#     new_post_vec = vectorizer.transform([new_post])
#
#     if 1 in new_post_vec.toarray():
#         np_array[count_j] = new_post_vec.toarray()
#         count_j += 1
#         continue
#     else:
#         So_Many_Fish+=[[re.sub('\s','',new_post), count_j]]
#     count_j += 1
#
# print(So_Many_Fish)


#np.savetxt('np_array.csv', np_array, delimiter=' ')

So_Many_Fish = [['是的', 5], ['是。', 85], ['你会死', 86], ['不', 87], ['你会死', 88], ['不', 89], ['你能死吗', 96], ['不', 97], ['不', 105], ['你会死', 108], ['不', 109], ['我挺好的，你呢', 129], ['那很好.', 131], ['是啊.', 132], ['那很好', 137], ['是啊', 138], ['你是谁?', 156], ['没了', 173], ['是的.', 178], ['是的.', 188], ['你有爱', 259], ['你会疯了吗', 301], ['你疯了', 313], ['你醉了', 327], ['不', 328], ['是的', 348], ['嗨', 368], ['嗨', 369], ['挺好', 376], ['挺好的', 378], ['挺好.', 388], ['我很好.', 396], ['我很好，你呢?', 398], ['没啥.', 414], ['钱', 642], ['是的', 709], ['枪', 734], ['是的', 743], ['你疯了', 755], ['你很忙', 756], ['你疯了', 776], ['是啊', 777], ['是的', 781], ['你疯了', 785], ['是的', 816], ['你是对的', 818], ['你疯了', 822], ['你是耐', 831], ['是的', 878], ['你让我疯了', 893], ['你疯了。', 898], ['你拿起', 903], ['你说', 918], ['你让我疯了', 921], ['你让我疯了。', 922], ['好了', 950], ['不', 1006], ['我到网。', 1012]]
So_Many_Fish_lb = []
So_Many_Fish_ask = []

for ll in So_Many_Fish:
    So_Many_Fish_lb += [ll[1]]
    So_Many_Fish_ask += [ll[0]]
np_arrays= np.loadtxt(open("chat/np_array.csv","rb"),delimiter=" ",skiprows=0)  #  单独调试需要改路径

new_post = None

def cost_dist(v1):

    np_acc = 0
    local_np = -1
    # print(' '.join(jieba.lcut(new_post)))  # 打印输入
    # print(new_post)                        # 打印输入
    input_lists = jieba.lcut(new_post)
    for i in input_lists:
        for j in range(58):
            if i == So_Many_Fish_ask[j] or new_post == So_Many_Fish_ask[j]:
                print(So_Many_Fish_lb[j])
                return content[So_Many_Fish_lb[j]+1]

        for j in range(1041):
            acc = 0
            lists = np.where(v1 == 1)[0].tolist()

            for ko in lists:
                if ko in np.where(np_arrays[j] == 1)[0].tolist():
                    acc+=1
            if acc > np_acc:
                np_acc = acc
                local_np = j

    return re.sub('\s','',content[local_np+1])

def chat_with_me(come_word):
    global new_post
    new_post = '{0}'.format(come_word)
    new_post_vec = vectorizer.transform([' '.join(jieba.lcut(new_post))])
    new_post_vec_array = new_post_vec.toarray()
    return cost_dist(new_post_vec_array[0])



