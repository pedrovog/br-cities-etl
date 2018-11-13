import os
from .save_obj import save_obj
import pkg_resources


def save_data(data):

    basepath = 'data/'

    if not os.path.exists(pkg_resources.resource_filename(__name__, basepath)):
        os.makedirs(pkg_resources.resource_filename(__name__, basepath))

    for key, value in data.items():
        path = '{}{}'.format(basepath, key)
        path = pkg_resources.resource_filename(__name__, path)
        if not os.path.exists(path=path):
            os.mkdir(path=path)
        for k, v in value.items():
            file_path = pkg_resources.resource_filename(__name__, '{}/{}/{}'.format(basepath, key, k))
            save_obj(v, file_path)
