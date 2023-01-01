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


def getkit(a):
    num = len(a)
    count = 0
    for i in range(num - 4):
        for j in range(i + 1, num - 3):
            for k in range(j + 1, num - 2):
                for l in range(k + 1, num - 1):
                    for m in range(l + 1, num):
                        kit = [a[i], a[j], a[k], a[l], a[m]]
                        count += 1
                        print(f'{count}/{num}', kit)
getkit(sorts)
