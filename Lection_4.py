# Сортировка подсчётом
def countsort(seq):
    minval = min(seq)
    maxval = max(seq)
    k = maxval - minval + 1
    count = [0] * k
    for now in seq:
        count[now - minval] += 1
    nowpos = 0
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1
    return seq


def countsort_2(a):
    cnt = [0] * (max(a) + 1)
    for item in a:
        cnt[item] += 1
    result = [num for num, count in enumerate(cnt) for i in range(count)]
    return result


def isdigitpermutation(x, y):
    '''
    x: Число
    y: Число
    output: Функция определяет можно ли получить первое число x из второго y перестановкой цифр (True/False)
    '''
    def countdigits(num):
        digitcount = [0] * 10
        while num > 0:
            lastdigit = num % 10  # используем остатки в качестве индексов
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount
    
    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True


def countbeatingrooks(rookcoords):
    '''
    N: N x N доска
    M: Количество ладей
    output: Функция выводит сколько пар ладей бьют друг друга
    '''
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol[key] += 1
        
    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs
    
    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)
