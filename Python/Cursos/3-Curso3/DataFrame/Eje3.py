from pandas import DataFrame;
dic={
    'word':['hello','world','python','ana'],
    'len':map(len,['hello','world','python','ana']),
    'starts':map(lambda x: x[0],['hello','world','python','ana']),
    'end':map(lambda x:x[-1],['hello','world','python','ana']),
    'is palindrome':map(lambda x: x==x[::-1],['hello','world','python','ana'])
}

df=DataFrame(data=dic);

dfc= df.copy();

dfc.columns=['palabra','longitud','inicio','fin','palindromo'];

print(dfc.head(3));
print(dfc.tail(3));

