from pandas import DataFrame;
from pandas import read_csv;
from pandas import read_json;

df=DataFrame(data=[[1,2,3],[4,5,6],[7,8,9]],columns=[1,2,3],index=[1,2,3]);

print(df);

df=DataFrame(data={'a':[1,2,3],'b':[1,2,3],'c':[1,2,3]},columns=['a','ab','b']);

print(df);

d = {"fila1": [1, 4, 7],
     "fila2": [2, 5, 8],
     "fila3": [3, 6, 9]}

df = DataFrame.from_dict(d, orient = "index", columns = ["A", "B", "C"])
print(df)

data=list(zip([1,2,3],[4,5,6]));

df=DataFrame(data,columns=['x','y']);

print(df);

dic={'x':[1,2,3],'y':[4,5,6]};

df=DataFrame.from_dict(data=dic,orient='columns');

print(df);

print(df.shape);

print(df.size);

print(df.ndim);

print(df['x']);

print(df[df.columns[1]]);

print(df.loc[:,'x']);

print(df.iloc[:,1]);

for i,j in df.iterrows():
     print('{}\n  {}'.format(i,j));
     
for i in df.itertuples():
     print('{}'.format(i));
     
#for i,j in df.iteritems():
#     print('{}\n  {}'.format(i,j));
     
df=read_csv('D:/Codigos/Python/Cursos/3-Curso3/DataFrame/179 characters-simpsons.csv');

print(df.head(10));

print(df.dropna())

     
df=read_json('D:/Codigos/Python/Cursos/3-Curso3/DataFrame/182 json_index_example.json',orient='index');

print(df.head(10));
