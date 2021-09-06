str = input()
if 'ABBA' in str or 'BAAB' in str:
    print('YES')
elif 'ABA' in str or 'BAB' in str:
    if str.count('AB') > 1 or str.count('BA') > 1:
        print('YES')
    else:
        print('NO')