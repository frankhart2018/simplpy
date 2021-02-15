import pandas


def read_tsv(file_path):
    return pandas.read_csv(file_path, sep="\t")
