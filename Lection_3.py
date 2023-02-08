# Multiset
setsize = 10
myset = [[] for _ in range(setsize)]


def add(x):
    myset[x % setsize].append(x)
    

def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            # xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i]
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
        

def twotermswithsumx(nums, x):
    '''
    nums: Последовательность положительных чисел длиной N
    x: Число
    output: Функция выводит 2 различных числа A, B из nums: A + B = x, иначе выводит пару 0, 0
    '''
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0


def wordsindict(dictionary, text):
    '''
    dictionary: Словарь из N слов, длина каждого не > K
    output: Функция определяет входит ли каждое слово в словарь (True or False)
    '''
    goodwords = set(dictionary)
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
        ans = []
        for word in text:
            ans.append(word in goodwords)
        return ans
