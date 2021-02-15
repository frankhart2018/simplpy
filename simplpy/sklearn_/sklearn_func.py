from ..dict_ import dict_sort


def sort_cr_by_support(cr, reverse=True):
    cr = cr.split("\n")
    cr_begin = cr[:2]
    cr_end = cr[-6:]
    cr_values = cr[2:-6]

    count_cr_values = {}

    for cr_value in cr_values:
        count = int(cr_value.split()[-1])
        if count in count_cr_values.keys():
            count_cr_values[count].append(cr_value)
        else:
            count_cr_values[count] = [cr_value]

    count_cr_values = dict_sort(count_cr_values, by="key", reverse=reverse)

    sorted_cr = "\n".join(cr_begin) + "\n"

    for i, cr_list in enumerate(count_cr_values.values()):
        for cr_value in cr_list:
            sorted_cr += cr_value + "\n"

    sorted_cr += "\n".join(cr_end)

    return sorted_cr
