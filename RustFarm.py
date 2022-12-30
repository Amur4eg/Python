with open(r'Source\seeds.txt', 'r') as f:
    sorts = list(map(lambda c: list(*c), [s.split() for s in f.readlines()]))


def genetic(gen):
    result = []
    strong = max(gen.values())
    for el in gen.keys():
        if gen[el] == strong:
            result.append(el)
    return result


def getresult(array):
    weight = {'W': 100, 'X': 100, 'G': 60, 'Y': 60, 'H': 60}
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


def getkit(array):
    pass


print(*sorts, sep='\n')
print()
print(*getresult(zip(*sorts)))
