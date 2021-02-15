from collections import OrderedDict


def dict_sort(dic, by="value", topk=None, reverse=True):
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
