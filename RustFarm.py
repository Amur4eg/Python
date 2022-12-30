sorts = [list(s) for s in input().split()]
print(sorts)


def genetic(gen):
    result = []
    strong = max(gen.values())
    for el in gen.keys():
        if gen[el] == strong:
            result.append(el)
    return result


def getresult(array):
    weight = {'w': 100, 'x': 100, 'g': 60, 'y': 60, 'h': 60}
    result = []
    for elm in array:
        res = dict()
        for c in elm:
            if c in res:
                res[c] += weight[c]
            else:
                res.setdefault(c, weight[c])
        result.append(genetic(res))
    return result