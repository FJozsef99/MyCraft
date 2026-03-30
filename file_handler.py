from config import *


def file_loader(path):
    with open(path, "r") as f:
        data = f.read()
    return data


# zippel lehetne a jövőben egyszerre menteni a mapot és az entity-ket

def matrix_saver(path, matrix):
    with open(path, "w") as f:
        for row in matrix:
            for i in row:
                f.write(str(i))
            f.write("\n")
