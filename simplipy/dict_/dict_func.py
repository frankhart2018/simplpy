from collections import OrderedDict

def dict_sort(dic, by="value", topk=None, reverse=True):
    if topk == None:
        topk = len(dic)

    if by == "value":
        return {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse=reverse)[:topk]}
    elif by == "key":
        return dict(OrderedDict(dic.items())[:topk])

def dict_counter(dic, key, value=1):
    if key in dic.keys():
        dic[key] += value
    else:
        dic[key] = value