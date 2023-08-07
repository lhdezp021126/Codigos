def avg(*list):
    sum=0;
    for e in list:
        sum+=e;
    return sum/len(list);
print(avg(1,2,3,4));