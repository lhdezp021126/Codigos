list1=['algo1',"algo2",'algo3','algo4'];
list2=[3,2,1,2,3,4];
list3=[1,3.2,'texto',True];

list1.append('algo5');

print(list1);

del list1[4];
print(list1);

list1.extend(list2);

print(list1);

list1.remove(1);

print(list1);

list2.sort()

print(list2);