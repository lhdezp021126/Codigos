def compare(n1,n2):
    if n1>n2:
        return 1;
    elif n2>n1:
        return -1;
    else:
        return 0;
print(compare(int(input('Insert a number: ')),int(input('Insert a number: '))));