global numbers;
numbers=[];

def fillOut():
    for i in range(5):
        numbers.append(int(input('Insert a number: ')));

def classify():
    par=[];
    impar=[];
    
    for i in numbers:
        if i % 2==0:
            par.append(i);
        else:
            impar.append(i);
    print('Par numbers: ',par);
    print('Impar numbers: ',impar);
        
fillOut();
classify();