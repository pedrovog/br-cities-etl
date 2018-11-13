from .load_obj import load_obj
import pkg_resources


def get_uf_mun_cod(state, city):

    path = 'data/{}/{}'.format(state, city)
    file_path = pkg_resources.resource_filename(__name__, path)
    data = load_obj(filename=file_path)

    print(data['UFMUN_COD'])
