import os
import numpy as np
from utils import *
import time
from BruteForce import without_pruning
from Pruning import with_pruning
from binary_programming import binary_prog
import pickle

def indicator_to_arrangment(indicator_matrix):
    neighbors = {}
    for i in range(0, indicator_matrix.shape[0]):
        for j in range(0, indicator_matrix.shape[1]):
            if indicator_matrix[i,j]==1:
                neighbors[concat_str(i,j)]=True
                neighbors[concat_str(j,i)]=True
    return neighbors

def recall(lst, indicator_matrix):
    neighbors = indicator_to_arrangment(indicator_matrix)
    den = len(lst)-1
    num=0
    for i in range(0,len(lst)-1):
        if neighbors.get(concat_str(lst[i], lst[i+1])) ==True:
            num+=1
        elif neighbors.get(concat_str(lst[i+1], lst[i])) ==True:
            num+=1
    return float(num/den)

def compute_interest_factor_from_indicator(indicator_matrix, interest_matrix):
    interest_factor = np.multiply(indicator_matrix, interest_matrix)
    interest_factor = interest_factor[np.nonzero(interest_factor)]
    min_interest = np.min(interest_factor)
    return np.sum(interest_factor)-min_interest

def main():
    file_path = "data\d_pet_pictures.txt"
    attributes = readfile(file_path)
    print("Total number of images", len(attributes))
    total_images = range(3,13)
    dump_lst = {}
    time_lst = []
    indicators = []
    num_images_lst = []
    best_perm = []
    best_interest_factor = []
    matrices = []
    # for i in range(0, len(total_images)):
    #     print("Current iteration is ", total_images[i])
    #     interest_matrix = create_interest_matrix(attributes[:total_images[i]])
    #     # interest_matrix = interest_matrix[:10, :10]
    #     # print(interest_matrix.shape)
    #     #
    #     start = time.time()*1000
    #     # indicator_matrix = binary_prog(interest_matrix)
    #     # interest_factor_bruteforce, best_bruteforce = without_pruning(attributes[:total_images[i]])
    #     # interest_factor_pruning, best_pruning = with_pruning(interest_matrix)
    #     # end = time.time()*1000
    #     # print("Time in ms", end-start)
    #     # time_lst.append(end-start)
    #     # best_perm.append(best_pruning)
    #     # num_images_lst.append(total_images[i])
    #     # best_interest_factor.append(interest_factor_pruning)
    #     matrices.append(interest_matrix)
    #     # dump_lst["time"] = time_lst
    #     # dump_lst[]
    #     dump_lst["interest_matrix"] = matrices
    #     # dump_lst["best_perm"] = best_perm
    #     # dump_lst["num_images"] =num_images_lst
    #     # dump_lst["best_interest_factor"] = best_interest_factor
    #     file = open("interest_matrix.pickle", "wb")
    #     pickle.dump(dump_lst, file)

    for i in range(0, len(total_images)):
        print("Current iteration is ", total_images[i])
        interest_matrix = create_interest_matrix(attributes[:total_images[i]])
        # interest_matrix = interest_matrix[:10, :10]
        # print(interest_matrix.shape)
        #
        start = time.time()*1000
        indicator_matrix = binary_prog(interest_matrix)
        # interest_factor_bruteforce, best_bruteforce = without_pruning(attributes[:total_images])
        # interest_factor_pruning, best_pruning = with_pruning(interest_matrix)
        end = time.time()*1000
        print("Time in ms", end-start)
        time_lst.append(end-start)
        indicators.append(indicator_matrix)
        num_images_lst.append(total_images[i])
        dump_lst["time"] = time_lst
        dump_lst["indicators"] = indicators
        dump_lst["num_images"] =num_images_lst
        file = open("binary_prog_results.pickle", "wb")
        pickle.dump(dump_lst, file)




if __name__=="__main__":
    main()
