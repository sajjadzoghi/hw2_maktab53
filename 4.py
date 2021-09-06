li = input()
if '-0' in li:
    print('Sorry! Please enter valid integers')
else:
    try:
        set = {int(i) for i in li.split()}
        print(set)
        n = input("Number of commands: ")
        if '-' in n:
            print('Sorry! Please enter a positive number.')
        elif '0' in n:
            print('So it seems you don\'t have any command!')
        else:
            n = int(n)
            if n > len(set):
                print('Number of commands are too much!')
            else:
                for i in range(n):
                    comm = input().split()
                    if comm[0] not in ['pop', 'remove', 'discard']:
                        print('Sorry! Invalid command!')
                    else:
                        if comm[0] == 'pop':
                            if comm[1] in set or comm[1] not in set:
                                print('Sorry! pop() doesn\'t accept any object.')
                            else:
                                set.pop()
                        elif comm[0] == 'remove':
                            if int(comm[1]) not in set:
                                print("Sorry! Remove a number existed in list.")
                            else:
                                set.remove(int(comm[1]))
                        elif comm[0] == 'discard':
                            set.discard(int(comm[1]))
                print(set)
    except ValueError:
        print('Sorry! Please enter valid integers')