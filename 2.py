"""tup1 = input().split()
tup1 = ''.join(tup1)
tup1 = tup1.split(',')
tup1 = ','.join(tup1)
print(set(eval(tup1)))"""

"""    elif i not in '-0123456789()':
        print('Sorry! Please enter a valid input.')
        break
(7, 3), (2, 1), (9, 7), (2, 17)
(1, 7), (6, 7), (8, 100), (4, 21), (7, 3)"""

def intersec(tup1, tup2):
    tup1 = tup1.split()
    tup1 = ''.join(tup1)
    tup1 = tup1.split(',')
    # --> ['(1', '7)', '(6', '7)', '(8', '100)', '(4', '21)', '(7', '3)']
    for i in tup1:
        if i == '(-0' or i == '-0)':
            return 'Sorry! Please enter a valid input.'
        elif i == '(-' or i == '-)':
            return 'Sorry! Please enter a valid input.'
        else:
            for ch in i:
                if ch not in '-0123456789()':
                    return 'Sorry! Please enter a valid input.'
    else:
        tup2 = tup2.split()
        tup2 = ''.join(tup2)
        tup2 = tup2.split(',')
        # --> ['(1', '7)', '(6', '7)', '(8', '100)', '(4', '21)', '(7', '3)']
        for i in tup2:
            if i == '(-0' or i == '-0)':
                return 'Sorry! Please enter a valid input.'
            elif i == '(-' or i == '-)':
                return 'Sorry! Please enter a valid input.'
            else:
                for ch in i:
                    if ch not in '-0123456789()':
                        return 'Sorry! Please enter a valid input.'
        else:
            tup1 = ','.join(tup1)
            tup1 = set(eval(tup1))
            tup2 = ','.join(tup2)
            tup2 = set(eval(tup2))
            return list(tup1 & tup2)


tup1 = input()
tup2 = input()
print(intersec(tup1, tup2))