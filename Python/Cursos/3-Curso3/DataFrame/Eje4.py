from pandas import DataFrame;
dic={
    'word':['hello','world','python','ana'],
    'len':map(len,['hello','world','python','ana']),
    'starts':map(lambda x: x[0],['hello','world','python','ana']),
    'end':map(lambda x:x[-1],['hello','world','python','ana']),
    'is palindrome':map(lambda x: x==x[::-1],['hello','world','python','ana'])
}

df=DataFrame(data=dic);

for i in df.itertuples():
    print('la palabra {}, es {} palindromo de {} letras'.format(i[1],'si' if i[5] else 'no',i[2]));
    