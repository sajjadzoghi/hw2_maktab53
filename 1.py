li = input()
if '-0' in li:
    print('Sorry! Please enter valid integers')
else:
    try:
        li = li.split(',')
        li = [int(number) for number in li]
        li.sort()
        li.reverse()
        prime = []
        other = []
        for number in li:
            s = 0
            for j in range(1, number + 1):
                if number % j == 0:
                    s += 1
            if s == 2:
                prime.append(number)
            else:
                other.append(number)

        print("prime=", prime)
        print("other=", other)
    except ValueError:
        print('Sorry! Please enter valid integers')
