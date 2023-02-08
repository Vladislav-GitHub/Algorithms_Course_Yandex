def main():
    seq = [1, 3, 2, 2, 4, 6, 2]
    print(findMinEven(seq))
    words = "Посмотрим, найдёшь ли ты слово я этого предложения."
    print(findShortWords(words))
    s = 'AAABBXCCCDDDDDDYZZH'
    print(rle(s))


def findMinEven(seq):
    '''
    seq: Последовательность чисел длиной N;
    output: Функция выводит минимальное чётное число в последовательности или -1, если такого не существует.
    '''
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (ans == -1 or ans > seq[i]):
            ans = seq[i]
    return ans


def findShortWords(words):
    '''
    words: Последовательность слов;
    output: Функция выводит все самые короткие слова через пробел.
    '''
    sentence = words.strip().split()
    minlen = len(sentence[0])
    
    for word in sentence:
        if len(word) < minlen:
            minlen = len(word)
    ans = []
    
    for word in sentence:
        if len(word) == minlen:
            ans.append(word)
    return ' '.join(ans)


def rle(s):
    '''
    s: Последовательность символов;
    output: Функция выводит символы и следом количество символов, если их больше 1, иначе сам символ.
    '''
    def pack(s, cnt):
        if cnt > 1:
            return s + str(cnt)
        return s
    
    lastsym = s[0]
    lastpos = 0
    ans = []
    
    for i in range(len(s)):
        if s[i] != lastsym:
            ans.append(pack(lastsym, i - lastpos))
            lastpos = i
            lastsym = s[i]
    ans.append(pack(s[lastpos], len(s) - lastpos))
    return ''.join(ans)


if __name__ == "__main__":
    main()
    