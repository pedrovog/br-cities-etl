import pandas as pd
import pickle
from br_cities_etl import save_obj, load_obj


# def save_obj(obj, filename):
#     with open(filename, 'wb') as f:
#         pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

# def load_obj(filename):
#     with open(filename, 'rb') as f:
#         return pickle.load(f)


if __name__ == "__main__":
    mun_file_path = 'datasets/cities.csv'
    uf_file_path = 'datasets/uf.csv'
    uf_mun_file_path = 'datasets/result/ufmun.csv'

    mun = pd.read_csv(
        mun_file_path,
        usecols=['Código Município Completo', 'Nome_Município', 'UF']
    )
    mun.columns = ['cod_uf', 'ufmun_cod', 'municipio']
    print(mun.head())

    uf = pd.read_csv(
        uf_file_path,
        usecols=['CD_GCUF', 'NM_UF_SIGLA']
    )
    uf.columns = ['cod_uf', 'uf']
    print(uf.head())

    uf_mun = mun.merge(uf)
    uf_mun = uf_mun[['uf', 'municipio', 'ufmun_cod']]
    uf_mun.columns = ['UF', 'MUNICIPIO', 'UFMUN_COD']
    print(uf_mun.head())

    uf_mun.to_csv(
        uf_mun_file_path,
        sep='|',
        encoding='utf-8',
        index=False
    )

    uf_mun_dict = uf_mun.groupby('UF').apply(
        lambda x: x.set_index('MUNICIPIO')[['UFMUN_COD']].to_dict('index')
    ).to_dict()

    save_obj(uf_mun_dict, 'datasets/result/ufmun.pkl')

    d = load_obj('datasets/result/ufmun.pkl')
    print(d)