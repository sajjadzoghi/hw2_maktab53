"""
((Sir, I've noticed that (like the example in question) if the sentence ends with "." ,so we may have some problem.
So I have fixed this problem in lines 11 to 15.))
"""
n = input("n: ")
if '-' in n:
    print('Sorry! Please enter a positive number.')
elif '0' in n:
    print('So it seems you don\'t have any dictionary!')
else:
    try:
        n = int(n)
        dic = {}
        for i in range(n):
            word = input()
            if ':' not in word:
                print('Sorry! I didn\'t see any ":".')
            else:
                word.split(': ')
                dic[word[0]] = word[1]
        sentence = input().split()
        for name in sentence:
            if '.' in name:
                w = sentence.index(name)
                d = name.find('.')
                sentence[w] = name[:d]
        for word in dic:
            if word in sentence:
                h = sentence.index(word)
                sentence[h] = dic[word]
        print(' '.join(sentence) + '.')
    except ValueError:
        print('Sorry! Please enter a positive number.')