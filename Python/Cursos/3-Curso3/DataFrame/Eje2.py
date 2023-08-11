from pandas import DataFrame;
dic={
    'word':['hello','world','python','ana'],
    'len':map(len,['hello','world','python','ana']),
    'starts':map(lambda x: x[0],['hello','world','python','ana']),
    'end':map(lambda x:x[-1],['hello','world','python','ana']),
    'is palindrome':map(lambda x: x==x[::-1],['hello','world','python','ana'])
}

df=DataFrame(data=dic);

dfc=df.loc[:,'starts':'is palindrome'];

for e in df.columns:
    print(df[e],end='\n\n\n');
   
print(dfc); 