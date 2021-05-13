from itertools import permutations
import os
import time
import math
import sys


# two integers into one
# def str_cat(a, b):
#     s1 = str(a)
#     s2 = str(b)
#     s = s1 + s2
#     return s


def with_pruning(interest_matrix):
    dict_store = {}
    num_images = interest_matrix.shape[0]
    combination = permutations(range(num_images))
    best_interest_factor = 0
    best_perm = None
    for single_perm in combination:
        # single_perm = combination[i]
        # print(single_perm)
        interest_factor = 0
        flag = False
        for j in range(len(single_perm) - 1):
            query = str(single_perm[j:])
            if dict_store.get(query):
                # print("here")
                interest_factor+=dict_store[query]
                flag = True
                break
            else:
                interest_factor+=interest_matrix[single_perm[j], single_perm[j+1]]
        if flag==False:
            temp = interest_factor
            for j in range(len(single_perm) - 2):
                query = str(single_perm[j+1:])
                temp += -1*interest_matrix[single_perm[j], single_perm[j+1]]
                if dict_store.get(query)==None:
                    dict_store[query] = temp
        if interest_factor > best_interest_factor:
            best_interest_factor = interest_factor
            best_perm = single_perm
    return best_interest_factor, best_perm
# open test for reading
# fp = open(sys.argv[1], "r")
#
# # Read existing file with plaintext passwords
# lines = [line.rstrip() for line in fp.readlines()]
#
# fp.close()
#
# # put photos in list
# photos = []
#
# # tags in each photos
# tags = []
#
# # put photos and tags in dictionary(ex.{1:["garden", "cat"], 2:["beach", "cat"]...})
# dic = {}
#
# # best combination
# slides = ()
#
# ID = 0
# maxIF = 0
# IF = 0
# IFCnt = 0
# tagCnt = 0
#
# # loop through each entry in lines to put it in dictionary
# for data in lines:
#     if ID != 0:
#         tags = []
#         tagCnt = data.split(" ")[1]
#         #print(tagCnt)
#         for i in range(2, int(tagCnt) + 2):
#             tags.append(data.split(" ")[i])
#
#         photos.append(ID)
#         #print("photos: ", photos)
#         dic[ID] = tags
#         #print("dic: ", dic)
#
#     ID += 1
#
#
# print("photos: ", photos)
# print("dic: ", dic)
#
#
# # interest factor tree dictionary
# IFtree = {}
#
#
#
#
# # list out keys and values separately
# dickey_list = list(dic.keys())
# dicval_list = list(dic.values())
#
# combination = permutations(photos)
#
# head = 0
# tail = 1
#
# length = len(photos)
#
# # permutation
# for slide in combination:
#     IF = 0
#     print(slide)
#
#     flag = 0
#
#     for i in range(length - 1):
#         flag = 1
#         for j in range(i + 1, length):
#
#             # only two photos
#             if flag == 1:
#                 k = concat(slide[j], slide[i])
#                 if k not in IFtree:
#                     IFtree[k] = interestfactor(dicval_list[slide[i] - 1], dicval_list[slide[j] - 1])
#                     twophotok = IFtree[k]
#                     k = concat(slide[i], slide[j])
#                     IFtree[k] = twophotok
#
#
#                 #print("photo: ", slide[i], slide[j])
#
#             # more than two photos
#             else:
#                 oldk = k
#                 k = concat(k, slide[j])
#                 if k not in IFtree:
#                     IFtree[k] = interestfactor(dicval_list[slide[j - 1] - 1], dicval_list[slide[j] - 1]) + IFtree[oldk]
#                 #print("photo:", slide[j - 1], slide[j])
#
#             flag = 0
#             IF = IFtree[k]
#             #print("k: ", k)
#             #print("IFtree: ", IFtree)
#
#             # slide
#             if i == 0 and len(str(k)) == length:
#                 IF = IFtree[k]
#                 if IF > maxIF:
#                     maxIF = IF
#                     slides = slide
#
#
# #print("IFtree: ", IFtree)
#
#
# # open file for writing in utf-8 encoding type
# fp = open("Slideshow.txt", "w", encoding="utf-8")
#
# fp.write((str(len(photos))))
# fp.write("\n")
#
# for i in range(len(photos)):
#     fp.write(str(slides[i]))
#     fp.write("\n")
#
# fp.close()
#
# print("maxInterestFactor: ", maxIF)
# print("slides: ", slides)
#
# # set end
# end = time.time()
#
# # count process time
# print("Process time = %d seconds" % (end - start))
