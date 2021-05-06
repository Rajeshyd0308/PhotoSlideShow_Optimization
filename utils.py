import os
import pandas as pd
import numpy as np


def readfile(filename):
    with open(filename) as file:
        text = file.readlines()
    i = 0
    attributes = []
    # time = []
    for i in range(0, len(text)):
        textline = text[i]
        temp = []
        if textline[0]=="H":
            attr = textline.split()
            temp.append(attr[2:])
            attributes.append(temp)
    return attributes

def compute_interest_factor(img1, img2):
    # print(img1)
    img1 = img1[0]
    img2 = img2[0]
    # print(img1)
    set1 = set(img1)
    set2 = set(img2)
    common_elements = set1 & set2
    return min(len(set1)-len(common_elements), len(common_elements), len(set2)-len(common_elements))


def create_interest_matrix(attributes):
    # print(attributes)
    num_images = len(attributes)
    interest_matrix = np.zeros((num_images, num_images))
    for i in range(0, num_images):
        # print(attributes[i])
        for j in range(i+1, num_images):
            interest_matrix[i,j] = compute_interest_factor(attributes[i], attributes[j])
            interest_matrix[j,i] = interest_matrix[i,j]
    return interest_matrix
