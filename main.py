import os
import numpy as np
from utils import readfile, create_interest_matrix

def main():
    file_path = "data\d_pet_pictures.txt"
    attributes = readfile(file_path)
    print("Total number of images", len(attributes))
    interest_matrix = create_interest_matrix(attributes[:5])






if __name__=="__main__":
    main()