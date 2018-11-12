import pickle

def load_obj(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)