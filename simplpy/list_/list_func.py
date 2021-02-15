def dump_list(List, filepath, sep="\n", mode="w"):
    with open(filepath, mode) as file:
        for item in List:
            file.write(str(item) + sep)
