import os
import pickle
import sys

sys.path.append('/home/rainersawitzki/git/org.javacream.training.python/src')


if __name__=='__main__':
    script_dir = os.path.dirname(os.path.realpath(__file__))
    data_file = script_dir + '/books_output.pickle'

    with open(data_file, 'rb') as f:
        print(pickle.load(f))
    

