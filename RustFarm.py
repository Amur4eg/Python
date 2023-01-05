with open(r'Source\seeds.txt', 'r') as f:
    seed = [s.strip() for s in f.readlines()]


def coast(char):
    """функция возвращает силу гена"""
    weight = {'W': 100, 'X': 100, 'G': 60, 'Y': 60, 'H': 60}
    if char in weight.keys():
        return weight[char]
    return 0


def deployments(array):
    """функция возвращает развернутый resylt из переданного array"""
    result = ['']
    for elm in array:
        if len(elm) > 1:
            result.extend(result)
            tmp = list(elm)
            for j in range(len(result)):
                if j >= len(result)/2:
                    result[j] += tmp[0]
                else:
                    result[j] += tmp[1]
        else:
            for i in range(len(result)):
                result[i] += str(*elm)
    return result


def genetic(kit):
    """функция возвращает result из переданного kit"""
    result, result = [], []
    for elm in zip(*kit):
        outgen, strong = set(), 0
        for gen in set(elm):
            if elm.count(gen) * coast(gen) >= strong:
                strong = elm.count(gen) * coast(gen)
        for gen in elm:
            if elm.count(gen) * coast(gen) >= strong:
                outgen.add(gen)
        result.append(outgen)
    return deployments(result)


def quality(seed):
    """функция возвращает оценку quality строки seed"""
    quality = 0
    for gen in seed.upper():
        if gen not in '(:)':
            quality += coast(gen)
    return quality


def getkit(array):
    num = len(array)
    count = 0
    for i in range(num - 4):
        for j in range(i + 1, num - 3):
            for k in range(j + 1, num - 2):
                for l in range(k + 1, num - 1):
                    for m in range(l + 1, num):
                        kit = [array[i], array[j], array[k], array[l], array[m]]
                        count += 1
                        print(f'{count}/{num}', kit)
                        print(genetic(kit)))


for s in seed.copy():
    print(f'{s}:{quality(s)}')
    if quality(s.upper()) >= 400:
        seed.remove(s)