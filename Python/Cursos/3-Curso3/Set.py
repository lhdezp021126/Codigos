A={1,2,3,4};
B={1,2,3,4,5,6,7,8};

print(A.issubset(B));
print(B.issuperset(A));

print(A|B);
print(A&B);
print(B-A);

A.add(9);
print(A);

A.update(B);

print(A);

