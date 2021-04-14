from PIL import Image
from numpy import asarray
from matplotlib import image
from matplotlib import pyplot
import os
import pickle

#This script is used to compile gif pics into a single txt file, the data is stored as binary data

def main():
    path = r"C:\Users\zhanglichuan\Desktop\Meng\ECE9039 Machine Learning\300"
    fileList = os.listdir(r"C:\Users\zhanglichuan\Desktop\Meng\ECE9039 Machine Learning\300")

    resultDic = list()    

    for i in fileList:
        file = os.path.join(path, i)
        img_data = image.imread(file)
        resultDic.append(img_data)
        

    with open('normal300.txt', 'wb') as data_file:
        pickle.dump(resultDic, data_file)

        
    with open('normal300.txt','rb') as read_file:
        img_list = pickle.load(read_file)

    pyplot.imshow(img_list[0])
    pyplot.show()

if __name__ == "__main__":
    main()
