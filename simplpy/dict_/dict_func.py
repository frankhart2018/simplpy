from collections import OrderedDict


def dict_sort(dic, by="value", topk=None, reverse=True):
    """
    Sort dictionary by key or value

    Params
    ======
    dic     (dict)
        : Input dictionary
    by      (str) 
        : String indicating the sorting procedure (value = sort by value, key = sort by key)
    topk    (int)(Optional)
        : Return top k results after sorting
    reverse (bool)(Optional)
        : Whether to return sorted array in ascending (reverse=False) or descending (reverse=True) order
    """

    if topk == None:
        topk = len(dic)

    if by == "value":
        return {
            k: v
            for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=reverse)[
                :topk
            ]
        }
    elif by == "key":
        return dict(OrderedDict(sorted(dic.items(), reverse=reverse)[:topk]))


def dict_counter(dic, key, value=1, append_value="int"):
    if append_value == "int":
        if key in dic.keys():
            dic[key] += value
        else:
            dic[key] = value
    elif append_value == "list":
        if key in dic.keys():
            dic[key].append(value)
        else:
            dic[key] = [value]
